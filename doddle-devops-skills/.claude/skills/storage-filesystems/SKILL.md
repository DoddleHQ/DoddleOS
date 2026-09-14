---
name: storage-filesystems
id: doddle.devops.storage
version: 1.0.0
blueprint: ./blueprint.yaml
description: Use for disk space incidents, new disk provisioning, partitioning (fdisk/parted, MBR/GPT), creating and checking file systems (mkfs/tune2fs/fsck), mounting and permanent mounts (fstab with UUIDs), and secure mount options. For volume resizing, RAID, or snapshots, see lvm-raid.
---

# Storage: Disks, Partitions, File Systems, Mounting

The full local-storage pipeline: discover the device → partition it → put a file system on it → mount it → make it permanent and secure. Every step verifies the previous one; every destructive command is double-checked against the device name.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Adding a new disk (virtual or physical) to a server
- Disk space incidents: full disks, wrong-size partitions, mount failures
- Creating/checking/tuning file systems (ext2/3/4, xfs, vfat)
- Making mounts permanent via /etc/fstab — safely, with UUIDs
- Hardening mounts (ro, noexec, nosuid)

## Initial Assessment

1. **Device**
   - What disks exist? `lsblk`, `fdisk -l`, `dmesg | grep sd[a-z]`
2. **Intent**
   - New storage, resize, fix a broken mount, or security hardening?
3. **File system**
   - Existing (`df -T`, `blkid`) or to be created? ext4 default, xfs for large/RHEL7-style.

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| task | string | yes | Provision / fix / harden storage; describe the goal |
| device | string | no | Disk or partition (ex /dev/sdb); discover via lsblk/fdisk -l if missing |
| mount_point | string | no | Target directory; create with mkdir if missing |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Storage layout before/after, commands run, verification |
| fstab_change | json | fstab line(s) added/changed with UUIDs (if any) |

---

## Core Framework

### Step 1: Discover
`lsblk`, `fdisk -l`, `dmesg | grep 'sd[a-z]'`, `cat /proc/partitions` (major/minor per device), `lsscsi` if available. Name the exact device before anything else.

### Step 2: Partition
`fdisk /dev/sdX` (n → p → size → t → w) or `parted /dev/sdX` (works directly on disk — no write step). GPT for >2TB or >4 partitions (`parted mklabel gpt`). Force kernel re-read after table changes: `partprobe`.

### Step 3: File system + mount
`mkfs.ext4 /dev/sdX1` → `mkdir /mount/point` → `mount /dev/sdX1 /mount/point` → verify `df -h`. Then make permanent in `/etc/fstab` using the UUID (`tune2fs -l /dev/sdX1 | grep UUID` or `blkid`).

---

## Detailed Guidance

### Device naming

- Modern Linux exposes scsi/sata/ssd/usb as `/dev/sdX` (sda, sdb… then sdaa). Partitions number from 1; logical partitions always start at 5.
- `ls -l /dev/sd*` shows `b` (block device) file type; `/proc/partitions` lists major:minor (8 = sd).
- Adding a disk with a lower address shifts names — the reason fstab uses UUIDs.

### Partitioning

- MBR: max 4 primary (or 3 + 1 extended holding logicals). Backup the MBR: `dd if=/dev/sda of=mbr.img bs=512 count=1` (logical drives need `sfdisk -d /dev/sda > parttable.sda`).
- GPT via parted: `mklabel gpt` (destroys existing table — confirmation required), `mkpart primary 0% 100%` for a whole-disk partition.
- fdisk writes only on `w` — you can back out with `q` until then. parted acts immediately.

### File systems

| FS | Create | Notes |
|----|--------|-------|
| ext2 | `mke2fs` | No journal; fsck after unclean shutdown |
| ext3 | `mke2fs -j` / `mkfs.ext3` | Journaling; convert ext2→ext3 with `tune2fs -j` |
| ext4 | `mkfs.ext4` | Default; large files/volumes, since 2008 |
| xfs | `mkfs.xfs` | RHEL7 default; scalable, high performance |
| vfat | `mkfs.vfat` | Cross-platform exchange media |
| swap | `mkswap` | Then `swapon` (see resource-monitoring) |

- Tune: `tune2fs -l` lists settings; `tune2fs -m <pct>` reserved-blocks (default 5% root reserve — set 0 on data-only volumes).
- Check: **unmount first**. `fsck` on a mounted fs warns SEVERE damage; after unmount `fsck -p /dev/sdX1` (preen). fstab's last field controls boot-time check order (1=root, 2=others, 0=none).

### Mounting + fstab

- Verify mounts three ways: `mount | grep <dev>`, `/proc/mounts` (kernel truth), `/etc/mtab` (maintained by mount — never hand-edit).
- `df -h` space per mount; `du -sh <dir>` usage per directory; `df -i` inodes (full inodes mimic full disk).
- fstab line: `UUID=... /mount/point ext4 defaults 0 2`. Test before reboot: `mount -a` (and `findmnt --verify` where available). `mount /mount/point` alone re-reads fstab.
- Remote: `mount -t nfs server:/srv/data /mnt/data`; cifs: `mount -t cifs -o user=... //host/share /mnt`.
- Mounting over a non-empty directory hides its files until umount; two filesystems on one mount point show only the last.

### Secure mount options

| Option | Effect |
|--------|--------|
| `ro` | Read-only |
| `noexec` | No binaries/scripts executable from the fs |
| `nosuid` | setuid bits ignored (bits still settable, not exploitable) |
| `noacl` | Disables ACL processing |

**Checklist (provisioning):**
- [ ] Device confirmed by size + `dmesg` before partitioning (wrong disk = data loss)
- [ ] Partition visible (`fdisk -l`) after `w`/partprobe
- [ ] `blkid`/`tune2fs -l` shows the new fs UUID
- [ ] `mount -a` clean after fstab edit; `df -h` shows expected size

**Checklist (incidents):**
- [ ] `df -h` AND `df -i` checked
- [ ] `du -sh` per top-level dir to find the consumer
- [ ] Deleted-but-held files: `lsof +L1` (see resource-monitoring)

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Partition the wrong disk | Instant data loss | Verify device via lsblk + dmesg + size first |
| fstab by /dev/sdX | Names shift on hardware change | UUID= entries |
| fsck on mounted fs | Severe corruption | Unmount (or rescue mode) first |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Edit fstab, reboot to test | Boot hangs on typo | `mount -a` + `findmnt --verify` before reboot |
| Skip parted GPT alignment | Performance warning | Use `%` positions or accepted alignment |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| "Disk full" without df -i | Inode exhaustion missed | Always both df -h and df -i |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Filesystem use | Used% per mount | <85% warn, <95% critical | df -h |
| Inode use | Used% inodes | <90% | df -i |
| Root reserve | % reserved blocks | 5% root fs; 0% data-only | tune2fs -l |

---

## Decision Tree

New disk → partition (fdisk MBR small / parted GPT large) → mkfs → mount → fstab by UUID → mount -a. Full disk → df -h + df -i → du -sh consumer or lsof +L1 → clean/extend (lvm-raid). Broken boot from fstab → rescue/live → mount root → fix fstab → mount -a.

---

## Quick Assessment Checklist

1. [ ] Device identified and confirmed?
2. [ ] Partitioning scheme (MBR vs GPT) chosen for size?
3. [ ] File system type selected for workload?
4. [ ] UUID captured for fstab?
5. [ ] Verification plan (mount -a, df -h) set?

---

## Expected Output Format

### Storage Layout
[Before/after: devices, partitions, mounts]

### Changes
[Commands, fstab lines with UUIDs, backups made]

### Verification
[df -h / mount output post-change]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| fstab typo blocks boot | Emergency shell at boot | Rescue boot, `mount -o remount,rw /`, fix line; next time test with mount -a |
| New partition invisible | fdisk -l missing it | `partprobe` / reboot |
| Files "vanished" after mount | Hidden under mountpoint | umount to access originals |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| (none) | Local shell execution via agent (fdisk/mkfs/mount) | — | — |

No external MCP bindings: storage state comes from local tools. Unavailable data is NOT AVAILABLE, never fabricated.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|-------------------|
| devops-surveyor | Before any change | lsblk/df/dmesg evidence |
| devops-analyst | Space incidents | Root cause: growth, inodes, held files |
| devops-operator | Approved changes | Partition/mkfs/fstab edits with backups + verification |

---

## Related Skills

- **lvm-raid**: Resizing volumes, mdadm RAID, snapshots
- **resource-monitoring**: lsof/iostat forensics on storage pressure
- **backup-restore**: Protect data before destructive steps

---

## Questions to Ask

1. Which device and what is the goal (provision/fix/harden)?
2. Expected size and file system type?
3. Permanent mount needed (fstab + UUID)?
