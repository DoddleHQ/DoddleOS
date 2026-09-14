---
name: process-management
id: doddle.devops.process
version: 1.0.0
blueprint: ./blueprint.yaml
description: Use when diagnosing runaway, hung, or zombie processes, CPU/memory hogs, or when a process must be signaled, reniced, or killed — covers ps/top/pgrep reading, signal semantics (TERM vs KILL, HUP, STOP/CONT), nice values, and job control (jobs/fg/bg/Ctrl-Z). For memory or I/O pressure analysis, see resource-monitoring.
---

# Process Management

Inspect, prioritize, signal, and control Linux processes. Exit codes and signal behavior are evidence — never guess at what a process is doing when `ps` and `/proc` can tell you.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- A process is runaway, hung, zombie, or eating CPU/memory
- A service must be stopped, reloaded, or killed — and the right signal matters
- Priority tuning (nice/renice) is needed to protect interactive or production work
- Jobs must be moved between foreground/background in a shell
- You need to identify a process by PID, name, parent, or terminal

## Initial Assessment

1. **Which process?**
   - Name or PID? Owner? Which terminal (`who am i`, `ps fax`)?
2. **What state?**
   - Running, sleeping, stopped, zombie (`STAT` column in `ps`)?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| symptom | string | yes | Process problem: runaway, hung, zombie, kill request |
| target | string | no | Process name or PID; discover via ps/pgrep if missing |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Process findings, action taken, verification |
| action_list | json | Signals sent / renices applied / jobs moved, with results |

---

## Core Framework

### Step 1: Inspect
`ps aux --sort=-%cpu | head -15`, `ps fax` for the process tree (parent/child), `pgrep -l <name>` for PIDs by name, `top -p <pid1>,<pid2>` to watch specific processes live.

### Step 2: Decide the signal
Match intent to signal — signal choice IS the decision (see table below).

### Step 3: Act and verify
Send the signal, then confirm with `ps`/`top` that the intended effect occurred and neighbours are healthy.

---

## Detailed Guidance

### Process facts

- Every process has a PID and a PPID (parent). `init`/`systemd` is PID 1 — the foster parent of orphans; it never dies.
- A process starts another via **fork + exec**; `exec` alone replaces without forking (same PID).
- A **zombie** is dead but still listed (parent hasn't reaped it). You cannot kill zombies — they are already dead; the fix is the parent.
- `$$` is your shell's PID, `$PPID` its parent — quick sanity anchors.

### Signals — the working set

| Signal | Num | Meaning | Use |
|--------|-----|---------|-----|
| SIGHUP | 1 | Re-read config | Reload daemons without restart (`kill -1 <pid>`, classic for init: `kill -1 1`) |
| SIGINT | 2 | Ctrl-C interrupt | Terminal interrupt |
| SIGTERM | 15 | Polite terminate (**default** for `kill`) | Always the first choice; process can clean up |
| SIGKILL | 9 | Kernel-enforced kill | Last resort — sent to the kernel, cannot be intercepted; no cleanup, possible data corruption |
| SIGSTOP | 19 | Suspend (freeze) | Process stays in memory, uses no CPU; also Ctrl-Z in shell |
| SIGCONT | 18 | Resume | Re-animate a stopped process |

`kill -l` lists all signals. Escalation order: TERM → wait → KILL.

**Checklist:**
- [ ] `kill <pid>` tried before `kill -9 <pid>`
- [ ] Target verified by PID before signaling (wrong PID = wrong victim)
- [ ] By name: `pkill <name>` (one) or `killall <name>` (all with that name)

### Priorities — nice values

- Lower nice = higher priority. Normal users can only raise their own processes' nice (0→20); only root may use negative values.
- Start with a nice: `nice -n 5 ./backup.sh`; change a running one: `renice +8 <pid>` (verify: `ps -C <name> -o pid,ni,comm`).
- **Careful**: negative nice values can make a box unusable (keyboard/ssh starved). Make less-important processes nicer to important ones, not the reverse.

### Job control (current shell)

- `jobs` / `jobs -p` (list with PIDs), `&` to background, Ctrl-Z to suspend (SIGSTOP), `bg %n` resume in background (SIGCONT), `fg %n` bring forward.
- Suspend by PID from elsewhere: `kill -SIGSTOP <pid>`; resume: `kill -SIGCONT <pid>`.

**Checklist:**
- [ ] `ps aux --sort=-%cpu|head` and `--sort=-%mem|head` run before any kill
- [ ] Zombie diagnosed as parent problem, not kill target
- [ ] Post-signal state confirmed with `ps -C` or `top -p`

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| kill -9 first | No cleanup, corrupt state | TERM first, KILL only after grace |
| Killing zombies | Already dead | Fix/restart the parent |
| Negative nice casually | Starves the system | Raise nice of unimportant work |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| killall by vague name | Mass collateral | pgrep -l first, then targeted kill |
| Ignoring STAT column | Misses stopped/zombie state | Read STAT in ps output |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Trusting one ps snapshot | Load is dynamic | top -p over a window |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Load average (1/5/15m) | Runnable + blocked processes | < cores sustained | uptime |
| Zombie count | Dead-unreaped processes | 0 sustained | ps aux, STAT Z |
| Top CPU process delta | Before/after renice | Stated in report | top -p |

---

## Decision Tree

Hung process → TERM, wait, verify → KILL only if still alive. Zombie → identify parent, restart parent. CPU hog (batch) → renice up, don't kill. Need reload not restart → HUP. Want it paused, not dead → STOP, later CONT.

---

## Quick Assessment Checklist

1. [ ] Target process identified (PID + name + owner)?
2. [ ] STAT/state checked (R/S/T/Z)?
3. [ ] Right signal chosen for intent?
4. [ ] Verification command planned?

---

## Expected Output Format

### Findings
[Process tree/state, evidence]

### Actions
[Signal/priority/job actions with results]

### Verification
[Post-action state]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| kill -9 left dirty state | Corrupt files/sockets on restart | Restore from backup; escalate via maintenance window |
| Process won't die even with -9 | D-state (uninterruptible I/O) | Wait on I/O; check hung disk/NFS; reboot last resort |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| (none) | Local shell execution via agent (ps/kill/nice) | — | — |

No external MCP bindings: all data comes from local process tools. Missing command output is stated NOT AVAILABLE, never fabricated.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|-------------------|
| devops-surveyor | Before any kill | ps/top evidence, process tree |
| devops-analyst | Recurring runaways | Root cause (leak, loop, schedule) |
| devops-operator | Approved signal/renice | Execution + verification |

---

## Related Skills

- **resource-monitoring**: Memory/I/O pressure behind process symptoms
- **boot-and-services**: Managing the service the process belongs to (systemd units)
- **kernel-modules**: strace/ltrace for what a process is doing

---

## Questions to Ask

1. Which process (name/PID), and what is the symptom?
2. Clean shutdown needed (TERM) or immediate (KILL)?
3. Should it be deprioritized instead of killed?
