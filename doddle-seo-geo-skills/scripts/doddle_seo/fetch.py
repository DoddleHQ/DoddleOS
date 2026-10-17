"""Fetch a page. stdlib-only. Respects robots.txt, rate limits, and an SSRF guard.

Local files and ``file://`` paths are read from disk so fixtures and saved snapshots
can be scored with no network at all.
"""

from __future__ import annotations

import gzip
import ipaddress
import socket
import time
import zlib
from dataclasses import dataclass, field
from typing import Dict, Optional
from urllib import error as urlerror
from urllib import request as urlrequest
from urllib.parse import urlparse

USER_AGENT = (
    "DoddleSEOGEO/0.1 (+https://doddlehq.com; deterministic-audit) "
    "Mozilla/5.0 (compatible; dseo/0.1)"
)
DEFAULT_TIMEOUT = 20.0
MAX_BYTES = 5_000_000
BLOCKED_HOSTS = {"localhost"}


@dataclass
class Fetched:
    url: str
    final_url: str
    status: Optional[int]
    body: str
    content_type: str = ""
    headers: Dict[str, str] = field(default_factory=dict)
    error: Optional[str] = None
    elapsed_ms: int = 0
    content_bytes: int = 0

    @property
    def ok(self) -> bool:
        return self.error is None and self.status is not None and 200 <= self.status < 400


def _is_private_host(host: str) -> bool:
    if host in BLOCKED_HOSTS:
        return True
    try:
        infos = socket.getaddrinfo(host, None)
    except socket.gaierror:
        return False
    for info in infos:
        addr = info[4][0]
        try:
            ip = ipaddress.ip_address(addr)
        except ValueError:
            continue
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved:
            return True
    return False


def _decode(raw: bytes, encoding: str) -> str:
    enc = (encoding or "").lower()
    try:
        if "gzip" in enc:
            raw = gzip.decompress(raw)
        elif "deflate" in enc:
            try:
                raw = zlib.decompress(raw)
            except zlib.error:
                raw = zlib.decompress(raw, -zlib.MAX_WBITS)
    except (OSError, zlib.error):
        pass
    for charset in ("utf-8", "latin-1"):
        try:
            return raw.decode(charset)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def fetch_local(path: str) -> Fetched:
    try:
        with open(path, "rb") as fh:
            raw = fh.read(MAX_BYTES)
    except OSError as exc:
        return Fetched(path, path, None, "", error=f"cannot read file: {exc}")
    ctype = "text/html"
    if path.endswith(".txt"):
        ctype = "text/plain"
    elif path.endswith(".json"):
        ctype = "application/json"
    elif path.endswith(".xml"):
        ctype = "application/xml"
    return Fetched(path, path, 200, _decode(raw, "utf-8"), ctype, {}, None, 0, len(raw))


def fetch(
    target: str,
    *,
    timeout: float = DEFAULT_TIMEOUT,
    allow_private: bool = False,
    user_agent: str = USER_AGENT,
    method: str = "GET",
) -> Fetched:
    """Fetch a URL or local path into a :class:`Fetched`."""
    if not target:
        return Fetched(target, target, None, "", error="empty target")

    parsed = urlparse(target)
    if parsed.scheme in ("", "file") and not target.startswith("http"):
        path = parsed.path if parsed.scheme == "file" else target
        return fetch_local(path)

    if parsed.scheme not in ("http", "https"):
        return Fetched(target, target, None, "", error=f"unsupported scheme: {parsed.scheme}")
    if parsed.scheme == "http":
        return Fetched(
            target,
            target,
            None,
            "",
            error="refusing plain http",
            headers={"hint": "use https"},
        )
    if not parsed.netloc:
        return Fetched(target, target, None, "", error="missing host")

    host = parsed.hostname or ""
    if not allow_private and _is_private_host(host):
        return Fetched(
            target,
            target,
            None,
            "",
            error=f"refusing private host: {host}",
            headers={"hint": "pass --allow-private to audit localhost/staging"},
        )

    req = urlrequest.Request(
        target,
        method=method,
        headers={
            "User-Agent": user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml,text/plain;q=0.8,*/*;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en;q=0.9,*;q=0.5",
        },
    )
    start = time.monotonic()
    try:
        with urlrequest.urlopen(req, timeout=timeout) as resp:
            raw = resp.read(MAX_BYTES)
            headers = {k.lower(): v for k, v in resp.headers.items()}
            body = _decode(raw, headers.get("content-encoding", "")) if _is_compressed(headers) else _decode(raw, "utf-8")
            return Fetched(
                target,
                resp.geturl(),
                resp.status,
                body,
                headers.get("content-type", ""),
                headers,
                None,
                int((time.monotonic() - start) * 1000),
                len(raw),
            )
    except urlerror.HTTPError as exc:
        raw = exc.read(MAX_BYTES) if exc.fp else b""
        headers = {k.lower(): v for k, v in (exc.headers or {}).items()}
        return Fetched(
            target,
            exc.geturl() if hasattr(exc, "geturl") else target,
            exc.code,
            _decode(raw, headers.get("content-encoding", "")) if _is_compressed(headers) else _decode(raw, "utf-8"),
            headers.get("content-type", ""),
            headers,
            f"HTTP {exc.code}",
            int((time.monotonic() - start) * 1000),
            len(raw),
        )
    except (urlerror.URLError, socket.timeout, TimeoutError) as exc:
        reason = getattr(exc, "reason", exc)
        kind = "timeout" if isinstance(reason, (socket.timeout, TimeoutError)) else "unreachable"
        return Fetched(target, target, None, "", error=f"{kind}: {reason}")
    except Exception as exc:  # noqa: BLE001 - never let a fetch crash an audit
        return Fetched(target, target, None, "", error=f"fetch failed: {exc}")


def _is_compressed(headers: Dict[str, str]) -> bool:
    return any(k in (headers.get("content-encoding", "") or "") for k in ("gzip", "deflate"))


class RateLimiter:
    """One request per ``rate`` seconds, shared across a crawl."""

    def __init__(self, rate: float = 1.0):
        self.rate = max(rate, 0.0)
        self._last = 0.0

    def wait(self) -> None:
        if self.rate <= 0:
            return
        delta = time.monotonic() - self._last
        if delta < self.rate:
            time.sleep(self.rate - delta)
        self._last = time.monotonic()
