---
name: networking-ssh
id: doddle.devops.networking
version: 1.0.0
blueprint: ./blueprint.yaml
description: Use for connectivity faults, interface and IP configuration (Debian /etc/network/interfaces, RHEL ifcfg files, ip/ifconfig), routing, arp, hostname, binding extra IPs, NIC bonding, ssh client/server setup incl. passwordless keys, packet sniffing (tcpdump), NFS shares, and basic iptables firewall checks. For service units like sshd, see boot-and-services.
---

# Networking and SSH

From the wire up: interfaces → addresses → routes → the services riding on top (ssh, NFS, firewall). Diagnose layer by layer, bottom to top — never debug DNS while the link is down.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Connectivity faults: no route, wrong IP, interface down
- Setting fixed IPs (Debian/RHEL), hostname changes, extra IPs (binding)
- NIC redundancy or throughput: bonding
- ssh access: connect, scp, passwordless keys, X forwarding, troubleshooting logins
- Packet-level proof: tcpdump/wireshark captures
- Sharing storage: NFS server exports + client mounts
- Firewall sanity: iptables status and rules

## Initial Assessment

1. **Layer check, bottom-up**
   - Link (`ethtool eth0` Link detected) → IP (`ip a`) → route (`ip r`/`route`) → DNS (`getent hosts name`) → service (`ss -tlnp`, `ping -c3 gateway` first)
2. **Distro family**
   - Debian (`/etc/network/interfaces`) vs RHEL (`/etc/sysconfig/network-scripts/ifcfg-*`)
3. **Change window**
   - Anything changed before it broke (ifcfg edit, firewall rule, switch port)?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| task | string | yes | Fix connectivity / configure IP / ssh setup / bonding / NFS / sniff / firewall |
| host_or_iface | string | no | Host, IP, or interface in question |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Layer findings, config changes, verification |
| config_change | json | Files edited (ifcfg/interfaces/fstab/exports) with rollback notes |

---

## Core Framework

### Step 1: Bottom-up diagnosis
Link (`ethtool`) → address (`ip a`) → gateway ping → DNS resolution → port (`ss`) → application.

### Step 2: Fix the lowest broken layer
Down interface: `ifup eth0` (reads config) or `ip link set eth0 up`. Missing route: `ip route add default via <gw>` then persist in config.

### Step 3: Prove each fix
Re-ping gateway → resolve name → connect service; capture with tcpdump when words aren't enough.

---

## Detailed Guidance

### Interface configuration — the modern view

- `ip a` (addresses), `ip r` (routes) — preferred; `ifconfig` remains everywhere. `ifconfig eth0` one card; `ifconfig eth0 up/down` keeps current config; `ifup/ifdown eth0` applies the **config file** (that's the difference that matters after edits).
- Temporary IP (until ifup cycle/reboot): `ifconfig eth0 192.168.33.42 netmask 255.255.0.0` — or `ip a add 192.168.33.42/16 dev eth0`.
- Hostname: `/etc/hostname` (Debian; also RHEL7+); runtime change `hostname <name>` or `sysctl kernel.hostname=<name>`; RHEL≤6: `/etc/sysconfig/network` HOSTNAME=.
- Port numbers: `/etc/services`; protocols: `/etc/protocols`.

**Debian** — `/etc/network/interfaces`:

```
auto lo
iface lo inet loopback
auto eth0
iface eth0 inet static
  address 10.42.189.198
  netmask 255.255.255.240
  gateway 10.42.189.193
```

(or `iface eth0 inet dhcp`); apply: `ifdown eth0 && ifup eth0`.

**RHEL** — `/etc/sysconfig/network-scripts/ifcfg-eth0`:

```
DEVICE="eth0"
HWADDR="08:00:27:DD:0D:5C"
NM_CONTROLLED="no"
BOOTPROTO="none"        # dhcp for client-mode
IPADDR="192.168.1.99"
NETMASK="255.255.255.0"
GATEWAY="192.168.1.1"
ONBOOT="yes"
```

Global `/etc/sysconfig/network` (HOSTNAME, GATEWAY on ≤RHEL6). RHEL7+: reload configs with `nmcli connection reload`; `nmtui` for guided edits. HWADDR pins a name to a NIC (≠ MACADDR which overrides the MAC — never both in one file).

- Extra IPs (binding): Debian adds `eth0:0` stanzas in interfaces (netmask mandatory); RHEL adds `ifcfg-eth0:0` files (DEVICE + IPADDR suffice); activate `ifup eth0:0`, verify `ifconfig | grep inet`.

### Routing, arp, neighbors

- View: `ip r` / `route` / `netstat -r`. Add default gw on the fly: `route add default gw 192.168.1.1` (lost on reboot unless in config).
- `arp -a` lists recent IP↔MAC neighbors (who you talked to); `arp -d host` clears an entry.

### Bonding (two NICs, one IP)

- RHEL: `/etc/modprobe.d/bonding.conf` (`alias bond0 bonding`), `ifcfg-bond0` (DEVICE/IPADDR/ONBOOT) + slave ifcfg-ethN files with `MASTER=bond0 SLAVE=yes`; `ifup bond0`.
- Debian: `aptitude install ifenslave`; interfaces stanza with `slaves eth1 eth2`, `bond-mode active-backup`, `bond-primary eth1`.
- Truth: `cat /proc/net/bonding/bond0` (mode, active slave, link failure counts).

### ssh — client and server

- Connect: `ssh user@host`; one command: `ssh user@host 'pwd'`; copy: `scp file user@host:/path` (both directions).
- Passwordless setup: `ssh-keygen -t rsa` (empty passphrase) → `ssh-copy-id -i ~/.ssh/id_rsa.pub user@host` (or append manually: `cat id_rsa.pub >> ~/.ssh/authorized_keys` — never overwrite). `.ssh` must be 700; private keys 600 or ssh refuses them.
- Debug a failing login: `ssh -v user@host` — read where it stops (connect / auth / keys).
- X forwarding: `ssh -X user@host` then run the GUI binary.
- Server: `openssh-server` package; config `/etc/ssh/sshd_config` — **Protocol 2 only**; host keys in `/etc/ssh/ssh_host_*` (public world-readable, private root-only). Agent: `ssh-add -L` lists loaded keys.
- Never use telnet/rsh/rlogin — credentials are sniffable; ssh encrypts the tunnel before authentication.

### Packet sniffing

- Quick CLI: `tcpdump host 192.168.1.38`, `tcpdump tcp port 22`, save `-w file`, replay `-r file`.
- wireshark for analysis: filter `icmp`, `dns`, `dns or icmp`, `ip.addr==10.1.2.3 and dns`; each packet's layer stack visible (eth:ip:udp:bootp). Capture on a quiet interface or with filters — full captures drown instantly.
- Sniffing proves what's really on the wire (e.g., plaintext protocols leaking credentials).

### NFS

- Server: `/etc/exports` entries — `/srv/iso *(ro,no_subtree_check)`, `/var/www pasha(rw) barry(rw,no_root_squash)`; `no_root_squash` maps remote root→nobody normally — only grant deliberately. Apply without restart: `exportfs -va`. Verify RPC services: `rpcinfo -p` (nfs 2049, mountd, nlockmgr).
- Client: `mount -t nfs server:/srv/data /mnt/data` + fstab `server:/srv/data /mnt/data nfs defaults 0 0`; nfs4 = tcp+2049, optional Kerberos.

### iptables sanity

- Status: `iptables -L -n` (or service iptables status) — INPUT/FORWARD/OUTPUT chains and rules; ruleset persisted at `/etc/sysconfig/iptables` (RH).
- Typical server posture: allow lo, established/related, then explicit NEW ports (22, 80…), REJECT the rest. A "connection refused everywhere" incident → check whether firewall policy changed before blaming services.

**Checklist (connectivity):**
- [ ] Link up (ethtool) → IP present (ip a) → gateway pings → name resolves → port listens (ss -tlnp)
- [ ] Config persisted (not just runtime `ip` commands)
- [ ] Change verified after ifdown/ifup cycle

**Checklist (ssh):**
- [ ] ssh -v output read on failures
- [ ] Key + .ssh permissions correct (700/600)
- [ ] Protocol 2 enforced server-side

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Debug DNS with link down | Wrong layer | Bottom-up: link → IP → route → DNS |
| Runtime-only fix | Lost at reboot | Persist in interfaces/ifcfg |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Overwrite authorized_keys | Locks out other keys | Append with >> |
| ifconfig up after editing config | Keeps old config | ifdown/ifup pair |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Trust service logs only | Packet truth stronger | tcpdump the port in question |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Gateway reachability | ping loss to gw | 0% loss | ping -c3 |
| Listener coverage | Expected ports listening | All expected | ss -tlnp |
| Bond health | Active slave present, 0 failures | Stable active | /proc/net/bonding |

---

## Decision Tree

No connectivity → link? → IP? → gw ping? → DNS? → port? → firewall. ssh fails → ssh -v locates stage → keys/permissions/protocol check. Need proof → tcpdump. Share dir → exports + exportfs -va → client mount + fstab.

---

## Quick Assessment Checklist

1. [ ] Distro family for config files known?
2. [ ] Lowest broken layer identified?
3. [ ] Persisted vs runtime change distinguished?
4. [ ] Rollback for config edits (backup file) ready?
5. [ ] Verification path (ping/ss/tcpdump) chosen?

---

## Expected Output Format

### Layer Findings
[Per-layer evidence]

### Changes
[Config files edited with backup paths]

### Verification
[Pings, ss output, ssh result, capture summary]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Keys rejected silently | Wrong .ssh perms | chmod 700 .ssh; 600 private key |
| Bond inactive after reboot | Missing alias/slave config | bonding.conf + SLAVE=yes files (RHEL) / ifenslave (Deb) |
| NFS mount hangs | Server RPC not listening | rpcinfo -p; exportfs -va |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| (none) | Local shell execution via agent (ip/ss/ssh/tcpdump) | — | — |

No external MCP bindings: network state is local. Unavailable data is NOT AVAILABLE, never fabricated.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|-------------------|
| devops-surveyor | First pass | ip/ss/ping/ethtool evidence |
| devops-analyst | Cross-layer faults | Which layer + what changed |
| devops-operator | Approved changes | Config edits (backed up) + verification |

---

## Related Skills

- **boot-and-services**: sshd/NFS/firewall as services
- **storage-filesystems**: NFS client mounting + fstab details
- **backup-restore**: ssh-piped backups across hosts

---

## Questions to Ask

1. Which host/interface and what broke (or what's the goal)?
2. Distro family (Debian/RHEL) for config style?
3. Is persistent configuration required, or runtime-only?
