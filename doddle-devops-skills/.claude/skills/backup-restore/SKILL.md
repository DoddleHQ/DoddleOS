---
name: backup-restore
id: doddle.devops.backup
version: 1.0.0
blueprint: ./blueprint.yaml
description: Use when files, partitions, or systems must be backed up, copied between servers, compressed, or restored — tar workflows (including over ssh), incremental backup levels, dump/restore, cpio with find, dd images and its dangers, split for oversized artifacts, and gzip/bzip2 trade-offs. For LVM snapshots as a backup source, see lvm-raid.
---

# Backup and Restore

Backups exist for the restore, not for the archive. Compression choice, backup levels, and safe extraction discipline — with the sharp edges of dd called out explicitly.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Backing up directories, configs, partitions, or whole disks
- Copying trees between servers (tar-over-ssh beats naive cp -r)
- Designing a level-based incremental rotation
- Restoring single files or full file systems from archives
- Creating images (dd): MBR, partition, CD-ROM ISO
- Splitting oversized artifacts for media limits

## Initial Assessment

1. **Scope**
   - Files/dirs (tar/cpio), file system (dump/restore), raw device (dd), or live volume (snapshot first → lvm-raid)
2. **Destination**
   - Local file, tape, or remote server (ssh pipe)
3. **Recovery objective**
   - What restore must look like (single file? bare metal?) — this picks the tool, not habit

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| task | string | yes | Backup or restore; source paths and destination |
| source | string | yes | Directory, partition, or device to protect/restore |
| destination | string | no | Archive path or remote host:dir; propose if missing |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Backup/restore actions, sizes, integrity verification |
| restore_plan | json | Archive inventory + tested restore steps + locations |

---

## Core Framework

### Step 1: Verify the source and free space
`df -h <dest>`, `du -sh <src>` — the archive must fit before you start.

### Step 2: Create with verification built in
tar with `v`; check result with `tar tvf` before calling it a backup.

### Step 3: Prove the restore
A backup is real only after a test extraction — restore one file to a staging path every time.

---

## Detailed Guidance

### Compression trade-off

| Tool | Speed | Ratio |
|------|-------|-------|
| gzip/gunzip | Fast | Good |
| bzip2/bunzip2 | Much slower (~100× on big files) | Better |

tar does it inline: `z` = gzip, `j` = bzip2.

### tar — the workhorse

| Task | Command |
|-----|---------|
| Create plain | `tar cf /backup/etc.tar /etc` |
| Create gz/bz2 | `tar czf /backup/etc.tar.gz /etc` / `tar cjf ...bz2` |
| Preserve perms | add `p` (`tar cpzf`) |
| List | `tar tvf archive` — one file: `tar tvf archive etc/resolv.conf` |
| Extract all | `tar xf archive` (current dir!) |
| Extract one file | `tar xvf archive etc/resolv.conf` |
| From a list | `find /etc -name "*.conf" > list` → `tar cpzf /backup/b.tgz -T list` |
| Via find | `find /etc -type f -name "*.conf" | xargs tar czf /backup/confs.tar.gz` |
| Copy a dir (faster than cp -r) | `(cd /etc; tar -cf - .) | (cd /backup/etc-copy; tar -xpf -)` |
| Copy over ssh | `(cd /etc; tar -cf - .) | ssh user@srv 'cd /backup/etc; tar -xf -'` |
| Compress only in transit | `cat backup.tar | ssh user@srv 'cat - > backup.tar'` (or let ssh do it: `ssh -C`) |

Exclude: `--exclude /etc/sysconfig`. tar strips leading `/` on create — restore paths are relative to cwd.

### Backup levels (incremental rotation)

Level 0 = full. Level N captures changes since the last level N-1. Example week: Mon 0 (full), Tue 1, Wed 2, Thu 3, Fri 3 (again — since last level 2), Sat 2 (since last level 1). Fewer fulls, bounded restore chains.

### dump/restore (file-system-aware)

- `dump` walks the ext file system itself (not a file list): `dump 0f /dev/nst0 /boot` then `dump 0f /dev/nst0 /` (level 0 to no-rewind tape). List: `dump -t`; compare: `dump -C`.
- Exclude a file even from fulls: `chattr +d /etc/hosts`.
- Restore: interactive/full `restore rf /dev/nst0` (into a mounted, empty fs), single subtree `restore -xf /dev/st0 /etc`.

### cpio + find

`find /etc -depth -print | cpio -oaV -O archive.cpio` (add `| gzip -c >` for compression); over ssh: `find /etc -depth -print | cpio -oaV | ssh user@host 'cpio -imVd'`; pull reversed: `ssh user@host "find path -depth -print | cpio -oaV" | cpio -imVd`.

### dd — powerful and dangerous

| Task | Command | Warning |
|-----|---------|---------|
| CD to ISO | `dd if=/dev/cdrom of=/path/cd.ISO` | safe (read) |
| MBR copy | `dd if=/dev/sda of=/MBR.img bs=512 count=1` | safe (read) |
| Wipe MBR | `dd if=/dev/zero of=/dev/sda bs=512 count=1` | DESTROYS partition table |
| Partition image | `dd if=/dev/sdb2 | gzip > /img/sdb2.IMG.gz` | restore needs same-ish geometry |
| Size a file | `dd if=/dev/zero of=file1MB bs=1024 count=1000` | — |

dd images restore only to very similar partitions/devices — not a portable backup. `of=/dev/sdX` typos are catastrophic: triple-check the target disk letter.

### split

`split -b 2000 bigfile part.` → `part.aa`, `part.ab`, … Rejoin: `cat part.* > bigfile`.

**Checklist (backup):**
- [ ] Destination free space ≥ source estimate
- [ ] Archive listed (`tar tvf`/`dump -t`) after creation
- [ ] One-file test restore performed
- [ ] dd targets verified by device letter before running

**Checklist (restore):**
- [ ] Archive integrity + inventory checked first
- [ ] Restored to staging path, not over live data, until validated
- [ ] Post-restore verification (file count, perms, app reads it)

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Backup without test restore | Untested = hypothetical | Extract one file every backup cycle |
| dd as general backup | Geometry-locked, blocky | tar/dump for files; dd only for images |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| tar xf into live dir | Overwrites current state | Staging directory first |
| dd of=/dev/sd? wrong letter | Instant destruction | Verify target via lsblk before Enter |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| bzip2 for nightly hot path | 100× slower for marginal gain | gzip for speed-critical, bzip2 for cold archive |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Backup success rate | Cycles with verified archive | 100% | tar tvf exit |
| Restore test | Last proven extraction | Every cycle | staged tar xvf |
| Archive size trend | Growth per cycle | Explained | ls -l archive |

---

## Decision Tree

Files/dirs → tar (levels for rotation) → verify with tvf. Whole fs → dump/restore. Pipes across hosts → tar/cpio over ssh. Raw image needed → dd + gzip, target triple-checked. Too big for medium → split.

---

## Quick Assessment Checklist

1. [ ] Scope + recovery objective stated?
2. [ ] Tool chosen to match (tar/dump/cpio/dd)?
3. [ ] Compression choice justified (speed vs ratio)?
4. [ ] Verification + test-restore planned?
5. [ ] Destructive-command targets verified?

---

## Expected Output Format

### Backup/Restore Record
[Commands, sizes, durations]

### Verification
[Archive listing summary, test-restore result]

### Restore Plan
[Exact steps to recover, archive locations]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| "Success" but archive empty | Wrong path order in tar | Always tar tvf after create |
| Restore garbled | dd image to unlike device | Match geometry or rebuild + file-level restore |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| (none) | Local shell execution via agent (tar/dump/dd/ssh) | — | — |

No external MCP bindings: archives are local/ssh operations. Unavailable data is NOT AVAILABLE, never fabricated.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|-------------------|
| devops-surveyor | Pre-backup | Source sizes, destination space |
| devops-analyst | Restore incidents | Which archive/level covers the loss point |
| devops-operator | Approved runs | Backup execution, staged restores, verification |

---

## Related Skills

- **lvm-raid**: Snapshots as consistent backup sources
- **storage-filesystems**: Devices and mounts being backed up
- **networking-ssh**: The ssh transport under remote backups

---

## Questions to Ask

1. What must be protected, and what does restore look like?
2. Local file, tape, or remote destination?
3. Retention/rotation policy (levels, count)?
