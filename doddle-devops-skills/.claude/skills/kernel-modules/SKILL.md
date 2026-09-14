---
name: kernel-modules
id: doddle.devops.kernel
version: 1.0.0
blueprint: ./blueprint.yaml
description: Use for kernel version and boot parameter inspection, kernel module loading problems (lsmod/modprobe/depmod, module dependencies, modprobe aliases), missing shared libraries (ldd), library tracing (ltrace), and syscall tracing (strace) to see what a program really does. For boot failures, see boot-and-services; for module-driven storage stacks, see lvm-raid.
---

# Kernel and Modules (with Library Tracing)

The kernel is a monolith with loadable modules (.ko) for drivers, file systems, and protocols. Underneath applications sit shared libraries (.so). This skill reads both layers: what the kernel loaded, and what a binary actually calls — ldd/ltrace/strace turn black boxes into evidence.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Checking kernel version or boot parameters (`uname -r`, `/proc/cmdline`)
- A module won't load, loads wrong, or hardware lacks its driver
- Module dependencies/aliases must be inspected or rebuilt
- "Library not found" / ldd shows missing shared objects
- You need proof of what a program does: library calls (ltrace) or syscalls (strace)
- Boot files (vmlinuz/initrd/System.map) need identification

## Initial Assessment

1. **Kernel or userspace?**
   - dmesg/module messages vs library/ldd errors — different layers, different fixes
2. **Version pinning**
   - `uname -r` — modules must match the *running* kernel's /lib/modules/<version>/
3. **What changed**
   - Kernel upgrade without reboot (modules dir mismatch), new hardware, updated libraries

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| symptom | string | yes | Module issue, missing library, or tracing request |
| target | string | no | Module name or binary path; discover if missing |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Kernel/module/library findings, actions, verification |
| trace_findings | json | ldd/strace/ltrace evidence summary |

---

## Core Framework

### Step 1: Identify the running kernel
`uname -r`; `/proc/cmdline` for boot params; `dmesg | tail` for recent kernel messages.

### Step 2: Inspect the module/library layer
`lsmod | grep <mod>`, `modinfo <mod>` (deps!), `ldd <binary>` (missing libs show plainly).

### Step 3: Fix with dependency-aware tools
modprobe (not insmod) for modules; reinstall owning package for broken libraries.

---

## Detailed Guidance

### Kernel facts

- Version: `uname -r` (ex 2.6.18-92.1.17.el5 — distro suffix). Boot params at runtime: `cat /proc/cmdline` (`ro root=... quiet`) — the ground truth of what grub passed.
- Boot files in /boot: `vmlinuz-*` (compressed kernel), `initrd/initramfs-*.img` (early-userspace drivers — a compressed cpio archive you can unpack and inspect), `System.map-*` (symbols; live copy /proc/kallsyms), `config-*` (compile options).
- Kernel log history: `/var/log/messages` kernel: lines survive reboots; `dmesg` shows current boot only.

### Modules — the working set

| Task | Command | Note |
|-----|---------|------|
| Loaded modules | `lsmod` (= formatted `/proc/modules`: size, use count, users) | Use count 0 = removable |
| Module info | `modinfo isdn` | Shows `depends:` — read it before loading |
| Load (dependency-aware) | `modprobe isdn` | Pulls deps (slhc) automatically; name only, no path |
| Load (raw, obsolete) | `insmod /path/isdn.ko` | Fails on missing deps ("Unknown symbol") |
| Remove | `modprobe -r isdn` | Also removes now-unneeded deps |
| Remove (raw) | `rmmod isdn` | Refuses while in use |
| Rebuild dep tree | `depmod` | Regenerates modules.dep after adding modules |
| Aliases/options | `/etc/modprobe.conf`, `/etc/modprobe.d/` | ex `alias eth0 pcnet32` |

- Modules live in `/lib/modules/<uname -r>/kernel/...` — a kernel update + no reboot means new modules dir while old kernel runs: builds and insmods must target the running version.
- Building one out-of-tree module: standard Makefile pattern `make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules`; load with insmod, verify with lsmod and `tail /var/log/messages`.

### Libraries and tracing (userspace)

- Shared objects live in /lib, /usr/lib; versioned files get major-version symlinks (libext2fs.so.2 → libext2fs.so.2.4).
- `ldd /bin/su` — dependency map; `not found` lines are the smoking gun for runtime errors.
- Repair: `dpkg -S libfoo.so.2` / `rpm -qf libfoo.so.2` → `debsums pkg` / `rpm -V pkg` → `aptitude reinstall pkg` / `yum reinstall pkg` → verify again.
- `ltrace -c -l /lib/libpam.so.0 su - user` — library call summary (which functions, how often, cost).
- `strace -o trace.txt <cmd>` — every syscall; grep the file for open/chmod failures. Example proof: vi writing a read-only file via `:w!` shows `chmod("42.txt", 0100400) = 0` — behavior no log will show you.

**Checklist (module won't load):**
- [ ] `modinfo` depends read; modprobe (not insmod) used
- [ ] Running kernel version matches module build (`uname -r`)
- [ ] `dmesg`/messages tail for the load attempt error

**Checklist (library error):**
- [ ] ldd run on the failing binary
- [ ] Owning package found and verified before reinstall
- [ ] Binary re-tested after repair

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| insmod with deps | "Unknown symbol" failure | modprobe |
| Manually place .so files | Invisible to package DB | Install/reinstall the package |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| rmmod an in-use module | Refused (or breaks users) | Check lsmod use-count; modprobe -r |
| Build against wrong headers | Module won't load on running kernel | Target /lib/modules/$(uname -r)/build |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Guessing program behavior | No evidence | strace/ltrace the actual run |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Module load failures | dmesg unknown-symbol count | 0 | dmesg |
| Missing libs | ldd "not found" count | 0 | ldd |
| Tainted modules | Proprietary loads flagged | Known + documented | lsmod (T flag), dmesg |

---

## Decision Tree

Module error → modinfo deps → modprobe → still failing? version match → depmod. Library error → ldd → owner query → verify → reinstall. "What is it doing?" → strace (syscalls) / ltrace (library calls) with -c summaries first.

---

## Quick Assessment Checklist

1. [ ] Running kernel version captured?
2. [ ] Module dependency chain known?
3. [ ] ldd evidence for library issues?
4. [ ] Trace output written to a file, not lost in scrollback?

---

## Expected Output Format

### Kernel/Module State
[Version, relevant loaded modules, deps]

### Evidence
[ldd/strace/modinfo excerpts]

### Actions + Verification
[What changed, re-test result]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Unknown symbol on load | Deps missing | modprobe; depmod after adding modules |
| lib not found at runtime | ldd shows gaps | Reinstall owning package |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| (none) | Local shell execution via agent (lsmod/ldd/strace) | — | — |

No external MCP bindings: kernel and library state are local. Unavailable data is NOT AVAILABLE, never fabricated.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|-------------------|
| devops-surveyor | Evidence base | lsmod/ldd/dmesg output |
| devops-analyst | Load/lib failures | Root cause + repair choice |
| devops-operator | Approved changes | modprobe/reinstall with verification |

---

## Related Skills

- **package-management**: Reinstalling packages that own libraries
- **boot-and-services**: initrd/kernel boot chain, module-load failures at boot
- **process-management**: The processes whose behavior traces explain

---

## Questions to Ask

1. Kernel- or userspace-side symptom?
2. Module name or binary path involved?
3. Recent kernel or package updates (version-skew risk)?
