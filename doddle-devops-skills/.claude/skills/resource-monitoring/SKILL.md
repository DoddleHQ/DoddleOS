---
name: resource-monitoring
id: doddle.devops.monitoring
version: 1.0.0
blueprint: ./blueprint.yaml
description: Use when the server is slow but CPU is idle, when memory pressure or OOM kills are suspected, when you need to know who holds a file or socket, or for baselining CPU/network/RAM/storage before trouble — free truth, vmstat/iostat/iotop reading, lsof/fuser forensics, swap management, sar history. For killing or renicing the process you find, see process-management.
---

# Resource Monitoring and Forensics

The four basic resources — CPU, network, RAM, storage — read correctly. Monitoring starts on day one so a baseline exists; diagnosis compares against it. Centered on the tools that answer "which resource, which process, since when".

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Server slow, CPU idle → I/O or memory hypothesis needs proof
- OOM kills suspected; memory leak hunting
- "Who holds this file/socket/port/mount?"; umount says target busy
- df and du disagree (deleted-but-held files)
- Swap setup (partition or file) or swap pressure analysis
- Baseline capture for capacity planning

## Initial Assessment

1. **Which resource?**
   - CPU (top/mpstat), memory (free/vmstat si-so), I/O (iostat/iotop), network (iftop)
2. **Window**
   - One snapshot lies — sample over 5+ intervals (`vmstat 2 5`)
3. **Baseline**
   - What does "normal" look like on this box? No baseline → record one now.

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| symptom | string | yes | Slow server, OOM suspicion, busy file/mount, baseline request |
| scope | string | no | Process/device/file to focus on |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Resource findings with sampled evidence, bottleneck verdict |
| baseline | json | CPU/mem/io/net reference values for future comparison |

---

## Core Framework

### Step 1: Sample the four resources
`uptime` + `top -b -n1 | head`, `free -m`, `df -h` + `df -i`, `iostat -x 2 5`, `vmstat 2 5`.

### Step 2: Name the bottleneck from the counters
`wa` high + disk `%util` pinned = I/O. `si/so` sustained = memory. `r`/`b` queues = CPU/runnable vs blocked. No counter moves = network or remote dependency.

### Step 3: Attribute to a process
`iotop -b -o -n 3`, `ps aux --sort=-%mem|%cpu`, `lsof`/`fuser` for holders.

---

## Detailed Guidance

### Memory — reading free correctly

- `free -m`: **available** is the number that matters, not "free" — buff/cache is reclaimable, not consumed. Low available + swap activity = real pressure.
- `/proc/meminfo` is the raw truth (MemTotal/MemFree/Buffers/Cached/SwapCached).
- Per-process swap: scan `/proc/[0-9]*/status` for VmSwap, sort descending.

### OOM forensics

- Kernel kill log is definitive: `dmesg -T | grep -i 'killed process\|out of memory'`, `journalctl -k | grep -i oom`.
- The killed process is the **symptom**; total pressure is the **cause**. Before restarting the victim: RSS growth over time (leak?), workload change, undersized box?

### vmstat — the small table with big answers

`vmstat 2 5` (use `-S M` for MB):

| Column | Meaning |
|--------|---------|
| `r` | Runnable queue (CPU-hungry) |
| `b` | Blocked on I/O |
| `swpd`/`si`/`so` | Swap used / swapped-in / swapped-out — si/so sustained = pressure |
| `bi`/`bo` | Blocks in/out (disk traffic) |
| `wa` | CPU idle-waiting on I/O |
| `us/sy/id` | User/system/idle CPU |

### iostat / iotop / mpstat / sar

- `iostat -x 2 5`: per-device `%util` (saturation) and `await` (latency ms). One device pinned at 100% util with high await while others idle = hot disk. `iostat -p sde` per-partition.
- `iotop -b -o -n 3`: names the I/O-hungry process (`-a` accumulates, `-u user` filters, `-p PID` one process).
- `mpstat -P ALL`: per-CPU breakdown (`%iowait`, `%soft`) — imbalance visible here, invisible in aggregate.
- `sar` (sadc data in /var/log/sa/saXX, cron-collected): history — `sar -u` CPU, `sar -r` memory, `sar -I PROC` interrupts. The only tool that answers "since when".
- Others: `top`/`htop` live, `watch -d free -om`, `nmon` all-round, `iftop`/`iptraf`/`ntop` for bandwidth per socket/host.

### lsof / fuser — who holds it

| Question | Command |
|----------|---------|
| Who has this file open | `lsof /var/log/app.log` |
| Deleted files still held (invisible usage) | `lsof +L1` |
| Who listens/connects on a port | `lsof -i :443` |
| Why umount fails | `fuser -v -m /mnt/share` — list first; `fuser -k` kills them (never before listing + proposing) |
| All files except root's | `lsof -u ^root` |

FD column: cwd/rtd/txt identity; r/w/u read/write/both.

### Swap management

- Inspect: `free -om`, `cat /proc/swaps` (device, size, used, priority).
- Add a swap **file**: `dd if=/dev/zero of=/swapfile bs=1024 count=20000` → `mkswap /swapfile` → `swapon /swapfile` → fstab line `/swapfile swap swap defaults 0 0`. Partition route: `mkswap /dev/sdX1` + `swapon`.
- Enable/disable at runtime: `swapon -a` / `swapoff` (needs free RAM to absorb pages).

**Checklist (slow server):**
- [ ] vmstat 2 5 sampled — wa/si/so/b read
- [ ] iostat -x 2 5 — per-device util/await
- [ ] iotop names a process for the traffic found
- [ ] OOM lines checked in dmesg before blaming the app

**Checklist (baseline):**
- [ ] CPU/mem/disk/net recorded under normal load, dated
- [ ] Stored where the next incident will find it

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Restart the OOM victim first | Cause is total pressure | Leak/workload/size analysis first |
| fuser -k reflexively | Kills innocent users of a mount | List, propose, then approved kill |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Single snapshot conclusions | Counters are rates | Sample 5 windows |
| Free-mem panic | buff/cache is healthy | Judge by available |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| df-vs-du mismatch unexplained | Deleted held files | lsof +L1 |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Load vs cores | 1m load / CPU count | < 1.0 sustained | uptime + nproc |
| wa / %util | I/O wait; device saturation | wa < 10; util < 80 sustained | vmstat, iostat |
| si/so | Swap movement | 0 sustained | vmstat |
| Available mem | free -m available | > 20% total | free |
| Disk use | per-mount used% | <85% (95% critical) | df -h |

---

## Decision Tree

Slow + idle CPU → vmstat: wa high → iostat finds device → iotop names process. si/so sustained → memory: OOM lines? → leak or undersized. Disk full, du disagrees → lsof +L1. umount busy → fuser -v → (approved) -k.

---

## Quick Assessment Checklist

1. [ ] Four resources each sampled (windowed)?
2. [ ] Baseline known or being recorded?
3. [ ] Bottleneck named from counters, not vibes?
4. [ ] Process attribution done (iotop/lsof)?
5. [ ] OOM evidence checked when memory is involved?

---

## Expected Output Format

### Findings
[Sampled counter evidence per resource]

### Bottleneck Verdict
[Resource + process + since-when if sar available]

### Recommendations
[Actions for other skills/agents, unresolved questions]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| OOM killer recurs | Random services die | Fix pressure source or add RAM/swap; never just respawn |
| Hot single disk | One %util=100 | Distribute or move the churning workload |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| (none) | Local shell execution via agent (vmstat/iostat/lsof/free) | — | — |

No external MCP bindings: counters come from local tools. Unavailable data is NOT AVAILABLE, never fabricated.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|-------------------|
| devops-surveyor | Always | The sampled evidence base |
| devops-analyst | Verdict | Bottleneck attribution, leak analysis |
| devops-operator | Follow-ups | Approved swap setup, process actions via process-management |

---

## Related Skills

- **process-management**: Acting on the process this skill identifies
- **storage-filesystems**: The disks whose counters are hot
- **scheduling-and-logging**: sar's cron collection; log-driven trends

---

## Questions to Ask

1. What is the symptom and since when?
2. Is there a baseline for this host?
3. Any recent changes (deploys, traffic, data growth)?
