---
name: boot-and-services
id: doddle.devops.boot
version: 1.0.0
blueprint: ./blueprint.yaml
description: Use for boot failures, bootloader (grub/grub2) configuration, kernel boot parameters, runlevel/init legacy systems, and every systemd task — why a service is dead or failing, enable/start/stop, targets, journal reading, boot-time analysis. For cron jobs, see scheduling-and-logging; for kernel modules, see kernel-modules.
---

# Boot, Services, and systemd

The path from power-on to a running server: POST → BIOS → MBR → bootloader → kernel → init/systemd → services. Master both halves: what happens before the OS (bootloader) and what the OS starts (systemd units).

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- A service is dead, masked, failing, or must be started/stopped/enabled
- Boot failures: grub errors, wrong root=, unbootable after changes
- Kernel parameters must change (single-user rescue, init=/bin/bash)
- Default boot target must change (multi-user vs graphical)
- Boot is slow and needs systemd-analyze blame
- Legacy SysV init systems (runlevels, chkconfig, /etc/inittab)

## Initial Assessment

1. **Which half?**
   - Pre-OS (bootloader/kernel messages) or service-level (systemd units)?
2. **Unit state**
   - `systemctl status <unit>`, `systemctl --failed`, `journalctl -u <unit> -n 50`
3. **Legacy?**
   - PID 1 tells: `ps -p 1` → systemd vs init; commands differ.

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| symptom | string | yes | Boot failure or service problem; what is observed |
| unit | string | no | systemd unit name; discover via systemctl --failed if missing |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Boot/service diagnosis, actions, verification |
| unit_change | json | enable/disable/mask/edit actions with rollback notes |

---

## Core Framework

### Step 1: Locate the failure in the boot chain
Pre-kernel (no grub menu → BIOS/boot device/MBR), kernel (panic, root= wrong), or userspace (`systemctl --failed`, journal).

### Step 2: Read the evidence at that layer
grub edit at boot (press `e`), `journalctl -b -p err`, `systemd-analyze blame` for slow boots.

### Step 3: Fix at the right layer, smallest change first
Config edit → syntax check → reload before restart → verify status and port.

---

## Detailed Guidance

### Boot chain

- POST → BIOS (boot device order) → MBR (first 512 bytes; `dd if=/dev/sda of=mbr.img bs=512 count=1` backs it up) → bootloader loads kernel + initrd → kernel runs → PID 1 (systemd on modern systems).
- Kernel boot params are visible at runtime: `cat /proc/cmdline`. Common rescues (edit grub entry with `e` at boot):
  - `single` — single-user mode (some distros still ask root password)
  - `init=/bin/bash` — raw root shell, no password (may be disabled at compile time)

### grub (legacy) essentials

- Config: `/boot/grub/grub.conf` (RHEL; menu.lst symlinked) — menu commands (`default`, `timeout`, `hiddenmenu`, `password --md5`) then stanzas:

```
title CentOS (2.6.32)
  root (hd0,0)
  kernel /vmlinuz-2.6.32 ro root=/dev/mapper/VolGroup-lv_root quiet
  initrd /initramfs-2.6.32.img
```

- hd0,0 = first disk, first partition. Chainloading another OS: `root (hd0,1)` + `makeactive` + `chainloader +1`.
- Install/repair: `grub-install /dev/sda`. Config edits need no reinstall (unlike lilo).

### grub2 essentials

- **Never edit `/boot/grub/grub.cfg`** — it is generated. Edit `/etc/default/grub` (GRUB_DEFAULT, GRUB_TIMEOUT, GRUB_CMDLINE_LINUX) and custom stanzas in `/etc/grub.d/40_custom`, then run `update-grub` (Debian family) or it happens on kernel install (RHEL: grub2-mkconfig -o /boot/grub2/grub.cfg).

### systemd — the working set

| Task | Command |
|-----|---------|
| Status | `systemctl status <unit>` (Loaded/Active/Sub + recent log lines) |
| Start/Stop/Restart | `systemctl start|stop|restart <unit>`; `reload` for config reload where supported |
| Enable/Disable (boot) | `systemctl enable|disable <unit>` — separate from start/stop |
| Mask (hard off) | `systemctl mask <unit>` |
| Failed units | `systemctl --failed` |
| All services | `systemctl -at service` |
| Targets (≈runlevels) | `systemctl list-units -t target`; switch: `systemctl isolate multi-user.target`; default: `systemctl enable multi-user.target --force` (rewrites default.target link) |
| Journal | `journalctl -u <unit> -n 50`, `journalctl -b -p err` (this boot, errors+), `journalctl -k` (kernel) |
| Power | `systemctl poweroff|reboot|halt|suspend` (replaces legacy commands) |
| Remote | `systemctl -H root@host status <unit>` |
| Boot time | `systemd-analyze blame` (per-service ms), `systemd-analyze` total |

- Dependencies live in `/etc/systemd/system/<target>.target.wants/` symlinks — that is what enable/disable manages.
- After editing a unit file: `systemctl daemon-reload` before restart.

### Legacy SysV (older boxes)

- `/etc/inittab`: `id:3:initdefault:` sets runlevel. Runlevels: 0 halt, 1 single-user, 3 multi-user server, 5 X11 desktop, 6 reboot (never 0/6 as default). `runlevel`/`who -r` show current; `telinit 3` (or `init 3`) switches.
- Start/stop: `/etc/init.d/<svc> start|stop|restart|status` or `service <svc> restart`. Boot enablement: `chkconfig <svc> on` / `--level 34` (RHEL) or `update-rc.d <svc> defaults` (Debian).
- Proper shutdown matters: `shutdown -h now` (halt), `-r` reboot, `+m` delayed; `last reboot` reads /var/log/wtmp history.

**Checklist (service down):**
- [ ] `systemctl status` + `journalctl -u` captured before restarting
- [ ] Config edited → syntax check (`nginx -t`, `sshd -t`) → `daemon-reload` if unit file touched
- [ ] reload attempted before restart (fewer dropped connections)
- [ ] Verified: status active + port listening (`ss -tlnp`) + real request

**Checklist (boot fix):**
- [ ] MBR/bootloader backed up before writes
- [ ] grub2 changes via /etc/default/grub + update-grub, never grub.cfg
- [ ] New kernel stanza tested with old stanza still present as fallback

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Restart before reading journal | Evidence destroyed on restart | status + journalctl first |
| Edit grub.cfg directly | Overwritten on next update | /etc/default/grub + update-grub |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| enable ≠ start confusion | Enabled but not running (or vice versa) | Do both explicitly; verify both states |
| Unit file edit without daemon-reload | Stale definition used | systemctl daemon-reload |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Only systemctl status | Sub-state missed | Read SubState + journal + `systemctl show <unit> | grep State` |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Failed units | Count at boot | 0 | systemctl --failed |
| Boot time | Userspace duration | Trend vs baseline | systemd-analyze |
| Restart count | Unit restarts from journal | Every restart explained | journalctl -u |

---

## Decision Tree

No grub menu → BIOS boot order/MBR. Kernel panic → grub edit `e`, check root= and initrd. Service failed → status + journalctl -u → config error? fix + reload → still failing? upstream (socket, dependency). Slow boot → systemd-analyze blame. Legacy box → init.d/chkconfig path.

---

## Quick Assessment Checklist

1. [ ] Pre-OS or service-level problem?
2. [ ] systemd (ps -p 1) or legacy init confirmed?
3. [ ] Journal evidence captured?
4. [ ] Reload-before-restart applied where supported?
5. [ ] Rollback path for boot changes (old stanza / MBR backup)?

---

## Expected Output Format

### Diagnosis
[Boot chain layer or unit + evidence]

### Actions
[Commands with output; backup paths]

### Verification
[Active state, port, request, boot result]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| fstab error blocks boot | Emergency/maintenance shell | `mount -o remount,rw /`, fix fstab, `mount -a`, reboot |
| Unit enters failed state | systemctl shows failed | journalctl -u; fix cause; `systemctl reset-failed` then start |
| Masked unit won't start | Start silently no-ops | unmask first |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| (none) | Local shell execution via agent (systemctl/journalctl/grub) | — | — |

No external MCP bindings: boot and unit state come from local tools. Unavailable data is NOT AVAILABLE, never fabricated.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|-------------------|
| devops-surveyor | First response | systemctl --failed, journal evidence |
| devops-analyst | Repeated failures | Root cause: config, dependency, timing |
| devops-operator | Approved changes | Unit/boot edits with backup + verification |

---

## Related Skills

- **scheduling-and-logging**: cron/logrotate units this service may own
- **networking-ssh**: sshd unit specifics + network-online ordering
- **process-management**: The process behind the unit (signals)

---

## Questions to Ask

1. Boot-time symptom or running-service symptom?
2. Which unit/host, and since when (change window)?
3. Legacy init possible (older distro)?
