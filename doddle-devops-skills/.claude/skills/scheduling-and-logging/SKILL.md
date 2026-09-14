---
name: scheduling-and-logging
id: doddle.devops.scheduling
version: 1.0.0
blueprint: ./blueprint.yaml
description: Use for one-time jobs (at), recurring jobs (cron/crontab, /etc/cron.*), and everything logging — who logged in (who/last/lastb), rsyslog routing by facility.priority, testing with logger, watching logs live, and rotating logs that eat disk. For service failures, see boot-and-services; for disk-full from other causes, see storage-filesystems.
---

# Scheduling and Logging

Two quiet workhorses of a server: jobs that run when you are asleep, and logs that tell you what happened while you were. Covers at/cron and the syslog stack end to end.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Scheduling one-off jobs (`at`) or recurring jobs (crontab, cron.d)
- Cron doesn't fire — permissions, allow/deny, environment, paths
- Logs are missing, misrouted, flooding, or eating the disk
- You need login history (who/last/lastb/lastlog) for audit
- rsyslog routing must change (new facility, remote logging)
- logrotate policy must be added or tuned

## Initial Assessment

1. **Schedule or log problem?**
   - Job didn't run / runs wrong, vs. log absent/wrong place/growing unbounded
2. **User or system scope?**
   - User crontab vs /etc/cron.d; app log vs rsyslog-managed
3. **Time correctness**
   - Server timezone/UTC vs user expectation — cron runs on local clock

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| task | string | yes | Schedule a job, fix a cron, route/rotate/audit logs |
| schedule | string | no | Cron expression or at-time; propose if missing |
| log_scope | string | no | Facility or log file in question |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Schedule/logging change, evidence, verification |
| jobs_registry | json | Jobs created/changed with schedules + owners |

---

## Core Framework

### Step 1: Classify
One-shot → `at`. Recurring user job → `crontab -e`. System/package job → `/etc/cron.d` or the /etc/cron.* directories.

### Step 2: Write the smallest correct schedule
Five fields (minute hour dom month dow), `*/n` steps, `@daily`-style macros. Absolute paths in commands — cron's PATH is minimal.

### Step 3: Verify it fires
`grep CRON /var/log/syslog` (or journalctl -u cron), then check the job's own output/redirect.

---

## Detailed Guidance

### at — one time jobs

- `at 22:01`, `at 10:05 tomorrow`, `at teatime tomorrow` → commands at the `at>` prompt, end with Ctrl-D.
- Queue: `atq` / `at -l`; remove: `atrm <id>`.
- Access: `/etc/at.allow` (if exists, only listed users) else `/etc/at.deny`; neither → everyone.

### cron — recurring jobs

Field order: **minute hour day-of-month month day-of-week** (`*` = all; dow 0 and 7 both Sunday).

| Example | Meaning |
|---------|---------|
| `8 14 * * * /usr/local/bin/script42` | Daily 14:08 |
| `25 0 1 * * /usr/local/bin/script8472` | Monthly, 1st, 00:25 |
| `*/2 * * * 0 /usr/local/bin/x` | Every 2 min, Sundays |

- Macros: `@reboot @yearly/@annually @monthly @weekly @daily/@midnight @hourly`.
- Edit user crontab only via `crontab -e` (never the spool files); list `crontab -l`; root inspects others: `crontab -l -u paul`; remove: `crontab -r`.
- System side: `/etc/crontab` runs `/etc/cron.hourly|daily|weekly|monthly` via run-parts (user field required); `/etc/cron.d/` for package-style entries needing finer control. RHEL-family uses anacron (`/etc/anacrontab`) for daily/weekly/monthly so missed jobs catch up.
- Access: `/etc/cron.allow` / `/etc/cron.deny` — same semantics as at.
- Cron debugging kit: syslog line written when each job fires; use absolute paths; redirect output (`>> /var/log/myjob.log 2>&1`); remember cron mails output if not redirected.

**Checklist (job didn't run):**
- [ ] `grep CRON /var/log/syslog | tail` — did cron attempt it?
- [ ] Executable bit + absolute path
- [ ] User allowed (cron.allow/deny)?
- [ ] Manually run the exact command line as that user

### Login logging (audit trail)

| File | Tool | Shows |
|------|------|-------|
| /var/run/utmp | `who` | Currently logged in |
| /var/log/wtmp | `last`, `last reboot` | Login history, reboots |
| /var/log/lastlog | `lastlog` | Last login per user (**Never logged in** markers) |
| /var/log/btmp | `lastb` | **Failed** logins (file may not exist; create + `chmod o-r` to enable safely) |
| /var/log/secure (RH) / auth.log (Deb) | grep | su/ssh failures — `Failed password`, `Invalid user` lines |

### rsyslog

- Selector = `facility.priority` → action. Facilities: auth, authpriv, cron, daemon, kern, lpr, mail, user, local0-7 (custom/appliances). Priorities ascending: debug < info < notice < warning < err < crit < alert < emerg.
- Selecting a priority includes all higher ones. Exact-only: prefix `=` (`local4.=crit`). Suppress: `.none`.
- Actions: file `/var/log/x` (prefix `-` to skip sync-per-write), `@remote-host` (forward), `user1,user2`, `*` (all logged-in users), named pipe `|`.
- Config lives in `/etc/rsyslog.conf` (+ /etc/rsyslog.d/); restart after changes (`service rsyslog restart` / systemctl).
- UDP reception (central log host): uncomment `$ModLoad imudp` + `$UDPServerRun 514`.

### logger + watching logs

- Test any routing: `logger -p local4.crit "l4 crit"` then read the target files — the fastest way to prove a selector works.
- Live: `tail -f /var/log/<log>`; repeat a command with change highlighting: `watch -d -n 3 '<cmd>'`.

### logrotate

- Main `/etc/logrotate.conf` (weekly, `rotate 4`, `create`, `dateext`, `compress` optional) + per-service files in `/etc/logrotate.d/`.
- Per-block overrides:

```
/var/log/myapp/*.log {
    weekly
    rotate 8
    compress
    missingok
    notifempty
    postrotate
        systemctl reload myapp >/dev/null 2>&1 || true
    endscript
}
```

- wtmp/btmp rotate monthly with special create modes (0664/0600 root utmp).

**Checklist (log eating disk):**
- [ ] logrotate entry exists for the file (`ls /etc/logrotate.d/`, grep the path)
- [ ] Rotation happens but app keeps writing to the old inode → reload/restart app in postrotate (or copytruncate)
- [ ] Flood source identified (which facility) before muting anything

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Cron for one-shot | Wrong tool | at |
| Mute a flooding log at rotation | Symptom treated, cause alive | Find the facility + fix the writer |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Relative paths in cron | Minimal PATH breaks lookup | Absolute paths everywhere |
| Skip rsyslog restart | New selectors never act | restart after conf change |
| logrotate without postrotate | App writes to rotated-away inode | reload in postrotate / copytruncate |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Reading btmp as logins | btmp = failures only | last for successes, lastb failures |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Cron fire rate | Jobs executed vs scheduled | 100% | syslog CRON lines |
| Failed logins | Spike vs baseline | Investigated spikes | lastb / auth log |
| Log growth | MB/day per busy log | Within rotation budget | du on /var/log |

---

## Decision Tree

One-shot → at; recurring → crontab -e (user) or cron.d (system). Job silent → syslog CRON grep → path/permission. Log missing → selector in rsyslog.conf? → restart → logger test. Log flooding disk → logrotate entry + postreload → then fix the writer.

---

## Quick Assessment Checklist

1. [ ] Schedule classified (at vs user cron vs cron.d)?
2. [ ] Timezone of the server confirmed?
3. [ ] Logging target file + facility identified?
4. [ ] logger test planned to verify routing?
5. [ ] Rotation owner (package vs custom) known?

---

## Expected Output Format

### Schedule/Logging Change
[Jobs or selectors added, exact lines]

### Evidence
[syslog/logger test output]

### Verification
[Job fired / log routed / rotation dry-run]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Cron silent | No CRON line in syslog | cron.allow check; crond running |
| Custom log empty | Selector wrong/not loaded | logger -p test; rsyslog restart |
| Disk full from one log | One file gigabytes | logrotate entry + postrotate reload; fix writer |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| (none) | Local shell execution via agent (cron/rsyslog/logrotate) | — | — |

No external MCP bindings: schedules and logs are local. Unavailable data is NOT AVAILABLE, never fabricated.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|-------------------|
| devops-surveyor | Log/schedule incidents | syslog, cron spool, logrotate state |
| devops-analyst | Floods and silent jobs | Root cause (facility, path, timing) |
| devops-operator | Approved changes | crontab/rsyslog/logrotate edits + verification |

---

## Related Skills

- **boot-and-services**: cron/rsyslog as systemd units
- **storage-filesystems**: /var/log on its own volume; disk-full handling
- **resource-monitoring**: Watching growth trends

---

## Questions to Ask

1. What must run, when (schedule), and as whom?
2. Which log/facility is the problem or target?
3. Rotation expectations (frequency, retention, compression)?
