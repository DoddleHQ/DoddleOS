---
name: package-management
id: doddle.devops.packages
version: 1.0.0
blueprint: ./blueprint.yaml
description: Use for installing, searching, upgrading, and removing software on Debian family (dpkg, apt-get, aptitude, apt) and Red Hat family (rpm, yum) — repository setup, which package owns a file, verifying and repairing installed files, converting packages with alien, and building from source. For broken dependencies or library errors, also see kernel-modules.
---

# Package Management

Two families, one discipline: Debian (.deb — dpkg/apt-get/aptitude/apt) and Red Hat (.rpm — rpm/yum). Repository front-ends resolve dependencies; the low-level tools verify and inspect. Same workflows on both sides.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Installing, removing, or upgrading software on any Debian/RHEL-family server
- "Which package owns this file?" / "is X installed?"
- Adding a third-party repository
- Verifying package file integrity (debsums / rpm -V) and repairing tampered files
- No package exists — building from source safely
- Cross-format need (alien rpm↔deb)

## Initial Assessment

1. **Family**
   - Debian/Ubuntu/Mint → apt; RHEL/CentOS/Fedora → yum/rpm
2. **Goal**
   - Install, survey, upgrade, verify, or repair?
3. **Source**
   - Official repos, third-party repo, local file, or source tarball — prefer repos always.

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| task | string | yes | Install/remove/upgrade/verify/build — name the software |
| package | string | no | Package name; search if unknown |
| source | string | no | Repo, local .deb/.rpm, or source tarball URL; default repos |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Package state before/after, commands, verification |
| change_record | json | Installed/removed/upgraded packages with versions |

---

## Core Framework

### Step 1: Sync index
`apt-get update` (Debian) / `yum makecache` (RH) before any operation.

### Step 2: Act through the dependency-aware front-end
apt-get/aptitude (Debian), yum (RH). Reserve dpkg/rpm for inspection and local files — they do not resolve dependencies.

### Step 3: Verify
Query the installed state (`dpkg -l pkg`, `rpm -q pkg`) and run the binary/version.

---

## Detailed Guidance

### Debian family

| Task | Command |
|-----|---------|
| List installed | `dpkg -l` (`ii` = installed, `rc` = removed-but-config, `un` = unknown/purged) |
| One package | `dpkg -l rsync` |
| Files of a package | `dpkg -L tmux` |
| Owning a file | `dpkg -S /etc/ssh/ssh_config` |
| Search repos | `apt-cache search rsync` / `aptitude search rsync` |
| Install | `apt-get install rsync` / `aptitude install rsync` (dependencies auto-resolved) |
| Remove | `apt-get remove rsync` (config kept — state rc) |
| Purge | `apt-get purge rsync` (config gone — state un) |
| Upgrade all | `apt-get upgrade` (Ubuntu: `aptitude safe-upgrade`) |
| Clean cache | `apt-get clean` (empties /var/cache/apt/archives) |

- Sources: `/etc/apt/sources.list` (+ sources.list.d). Same config serves apt-get, aptitude, apt — add a repo once, all tools see it.
- Local .deb: `dpkg -i file.deb` (dependencies manual) — prefer repo install when possible.

### Red Hat family

| Task | Command |
|-----|---------|
| List installed | `rpm -qa` |
| One package | `rpm -q gcc` |
| Owning a file | `rpm -qf /lib/libext2fs.so.2` |
| Files of a package | `rpm -ql pkg` |
| Verify files | `rpm -V pkg` (S size, T mtime flags per file; clean = silence) |
| Search | `yum search gcc44` |
| Which package provides a file | `yum provides */passwd.5.gz` |
| Install / Update | `yum install sudo` / `yum update` / `yum update sudo` |
| Groups | `yum grouplist`, `yum groupinstall 'Sound and video'` |
| Local .rpm | `rpm -Uvh pkg.rpm` (U = upgrade-or-install; vh = progress) |
| Remove | `rpm -e pkg` — refuses while dependencies exist (safety) |

- Repos: `/etc/yum.conf` + `/etc/yum.repos.d/*.repo` (`[repo] name= baseurl= gpgcheck=1 gpgkey=`). Enable ad-hoc: `yum install x --enablerepo=repo`.
- rpm database lives in `/var/lib/rpm`.
- Peek inside an rpm without installing: `rpm2cpio pkg.rpm | cpio -t` (list) / `cpio -iv <file>` (extract one).

### Cross-family and verification

- `alien --to-deb pkg.rpm` converts rpm→deb (experimental — prefer native packages).
- Repair a broken/modified library file: find owner (`dpkg -S`/`rpm -qf`) → verify (`debsums pkg`/`rpm -V pkg`) → reinstall (`aptitude reinstall pkg` / `yum reinstall pkg`) → verify again (silence = clean).

### Building from source

1. Read the README first — always.
2. Inspect where it wants to install: `tar tvzf app.tgz`
3. `tar xzf app.tgz` (j for .tar.bz2) → cd into dir
4. `./configure` → `make` → `make install` (root for the last)
5. Caveat: outside the package database — upgrades/uninstall are manual; prefer distro packages when they exist.

**Checklist:**
- [ ] Index refreshed this session
- [ ] Front-end (apt/yum) used, not raw dpkg/rpm -i, when dependencies matter
- [ ] Installed state + binary run verified after install
- [ ] Third-party repo has gpgcheck
- [ ] Source builds recorded (path, configure flags) for future removal

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| dpkg/rpm -i from repos' era | Dependencies unresolved | apt/yum install |
| Source install when package exists | Invisible to package DB | Prefer packages |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| apt-get upgrade on stale index | Old versions resolved | update first |
| rpm -e past dependencies | Breaks other packages | Respect the refusal; remove dependents first |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| rc state read as installed | Config-only leftover | Purge to finish removal |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Pending updates | Upgradable count | Applied within policy window | apt-get upgrade / yum check-update |
| Failed verifications | debsums/rpm -V diffs | 0 unexplained | debsums, rpm -V |
| Cache size | /var/cache/apt/archives | Bounded | du + apt-get clean |

---

## Decision Tree

Install → repos first (search → install) → local file second (dpkg -i/rpm -Uvh) → source last (README → configure → make → make install). Missing library at runtime → owner query → reinstall owner. File integrity doubt → verify → reinstall → re-verify.

---

## Quick Assessment Checklist

1. [ ] Distro family confirmed?
2. [ ] Index fresh?
3. [ ] Package name known or searched?
4. [ ] Source preference order respected (repo > file > source)?
5. [ ] Verification command chosen?

---

## Expected Output Format

### Package State
[Before/after, versions]

### Actions
[Exact commands + output]

### Verification
[Query + binary run]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Dependency error on rpm -e | Listed dependents block | Remove/update dependents or use yum remove |
| make fails on fresh box | No compiler/headers | Install build group (yum groupinstall 'Development Tools' / apt build-essential), retry |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| (none) | Local shell execution via agent (apt/yum/rpm/dpkg) | — | — |

No external MCP bindings: package state is local. Unavailable data is NOT AVAILABLE, never fabricated.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|-------------------|
| devops-surveyor | Before changes | Installed state, pending updates |
| devops-analyst | Broken installs | Dependency/library root cause |
| devops-operator | Approved changes | Install/remove/reinstall with verification |

---

## Related Skills

- **kernel-modules**: ldd/library errors after installs; module builds
- **boot-and-services**: New package installed a service — enable + verify
- **storage-filesystems**: /var/cache growth management

---

## Questions to Ask

1. Which software, on which distro family?
2. From repos, a local file, or source?
3. Any policy on upgrade windows?
