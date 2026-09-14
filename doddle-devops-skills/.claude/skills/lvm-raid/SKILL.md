---
name: lvm-raid
id: doddle.devops.lvm
version: 1.0.0
blueprint: ./blueprint.yaml
description: Use for LVM volume inspection, extension (online lvextend + resize2fs), resizing physical volumes, mirrors and snapshots, mdadm software RAID state checks and rebuilds, and disk-capacity incidents on volume-managed servers. For basic partitioning or fstab work, see storage-filesystems.
---

# LVM and Software RAID

LVM puts a virtual layer between mounted file systems and hardware: volumes can grow while mounted, data can migrate off failing disks, snapshots freeze a point in time. RAID (mdadm) adds redundancy underneath. Together they are the standard Linux storage stack for servers.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- A file system needs more space and unmounting is not acceptable
- Inspecting or verifying existing PV/VG/LV layouts (`pvs`/`vgs`/`lvs`)
- Creating volumes, mirrors, or snapshots; migrating data with pvmove
- Checking mdadm RAID health (`/proc/mdstat`), replacing failed members
- Capacity planning on volume-managed servers

## Initial Assessment

1. **Current stack**
   - `lsblk` (partitions, lvm type, raid), `pvs`, `vgs`, `lvs`, `cat /proc/mdstat`
2. **Goal**
   - Extend, create, migrate, snapshot, or repair?
3. **Free space**
   - VG free extents (`vgs` VFree) — is there room, or must a PV be added first?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| task | string | yes | Extend volume, create LV/VG, snapshot, mirror, pvmove, RAID check/repair |
| volume | string | no | VG/LV path (ex vg0/data) or md device (/dev/md0); discover via lvs/mdstat |
| size | string | no | Amount (ex +10G, or absolute 50G); ask if missing for extends |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Volume/RAID layout before/after, commands, verification |
| capacity_plan | json | Free/used extents, growth steps, rollback notes |

---

## Core Framework

### Step 1: Map the stack
Physical volumes → volume groups → logical volumes: `pvs`/`pvdisplay`, `vgs`/`vgdisplay`, `lvs`/`lvdisplay`. RAID under it: `cat /proc/mdstat`, `mdadm --detail /dev/mdX`.

### Step 2: Change at the right layer
Extend order: add PV → extend VG → extend LV → resize file system. Never skip the last step — df will not change until resize2fs/xfs_growfs runs.

### Step 3: Verify
`lvs` shows new LV size, `df -h` shows the file system grew, mount still healthy.

---

## Detailed Guidance

### LVM lifecycle

| Operation | Command |
|-----------|---------|
| Make PV | `pvcreate /dev/sdb1` (or whole disk — but a partition spanning the device is friendlier to other OSes) |
| Create VG | `vgcreate vg42 /dev/sdb1 /dev/sdc` |
| Create LV | `lvcreate -L 200M -n data vg42` (also `-l 10%VG`, `-l 30%FREE`) |
| Extend LV | `lvextend -L +100M /dev/vg42/data` or `-l +50%LV` |
| Grow fs online | `resize2fs /dev/vg42/data` (ext; mounted OK) — xfs: `xfs_growfs <mount>` |
| Remove | `lvremove vg42/data` → `vgremove vg42` → `pvremove /dev/sdb1` |
| Add PV to VG | `vgextend vg42 /dev/sdd` |
| Remove PV (after emptying) | `pvmove /dev/sdd` then `vgreduce vg42 /dev/sdd` |
| Rescan PV size | After resizing its partition: `pvresize /dev/sdd1` |
| Mirror | `lvcreate -L 300m -m 1 -n lvmir vg33` (needs 3 PVs: 2 legs + log) |
| Snapshot | `lvcreate -L 100M -s -n snap vg42/data` |
| Block re/allow alloc | `pvchange -x n|y /dev/sdd` |

Classic gotcha: after `lvextend`, `df -h` still shows the old size — the file system was never resized. `resize2fs` closes the gap; ext supports online growth.

### Snapshots

- A snapshot LV retains original blocks as the origin changes — `lvs` Snap% shows divergence. When Snap% approaches 100%, the snapshot breaks: size it for the rate of change over the backup window.
- Workflow: snapshot → `tar`/`dump` the snapshot device → `lvremove vg42/snap`. Restores a consistent point-in-time copy of a live volume.

### RAID (mdadm)

- Levels: 0 stripe (no redundancy), 1 mirror, 5 striped parity ≥3 disks (survives one loss), 6 dual parity (survives two), 1+0 stripe of mirrors. 0+1 and 5+0 exist; raid4's dedicated parity disk bottlenecks — rare.
- Partition type `fd` (Linux raid autodetect) on members.
- Create: `mdadm --create /dev/md0 --level=5 --raid-devices=3 /dev/sdb1 /dev/sdc1 /dev/sdd1`
- State: `cat /proc/mdstat` (`[UU_]` = degraded, recovery % shown), detail: `mdadm --detail /dev/md0` (State clean/degraded, per-member sync)
- Replace member: `mdadm /dev/md0 --add /dev/sde1 --fail /dev/sdb1 --remove /dev/sdb1`
- Teardown: `mdadm --stop /dev/md0` then repartition members.

### iSCSI + multipath (adjacent — know when to call it)

- Remote block storage = iSCSI: target (server, LUNs) vs initiator (client). Modern target config via `targetcli` (backstores → iscsi target → ACLs → LUNs; saveconfig). Initiator: `/etc/iscsi/iscsid.conf` CHAP creds, `iscsiadm -m discovery -t st -p <ip>` then `-l` to log in — new /dev/sdX devices appear, then treated as normal disks.
- Multiple paths to the same LUN → device-mapper-multipath: `mpathconf --enable`, `multipath -ll` (round-robin groups, active/enabled paths), use `/dev/mapper/mpathX`.

**Checklist (extend):**
- [ ] `vgs` free space confirmed (or PV added first)
- [ ] `lvextend` and `resize2fs`/`xfs_growfs` both planned
- [ ] df -h before/after recorded

**Checklist (RAID):**
- [ ] `/proc/mdstat` `[UUU]` state checked first
- [ ] Failed member replaced with --add/--fail/--remove sequence
- [ ] Rebuild progress monitored before removing anything else

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| lvextend without resize2fs | df unchanged, "extension failed" illusion | Always pair LV + fs resize |
| pvremove a busy PV | Data loss | pvmove first, vgreduce after |
| Undersized snapshot | Snap% hits 100, snapshot drops | Size for change-rate × window |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Shrinking online | ext shrink needs umount + fsck | Grow only online; shrink via maintenance window |
| Two RAID ops at once | Double fault risk | One member replace + full rebuild at a time |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Reading df for LV size | df shows fs, not volume | lvs/lvdisplay for LV truth |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| VG free | Free extents per group | >20% headroom | vgs |
| Snapshot usage | Snap% per snapshot LV | <80% | lvs |
| RAID health | Members in sync | [UUU…] all-U | /proc/mdstat |
| Rebuild progress | recovery % | Completes without second fault | /proc/mdstat |

---

## Decision Tree

Need space → VG free? → yes: lvextend+resize → no: pvcreate+vgextend first. Failing disk in VG → pvmove → vgreduce → pvremove. Consistent backup of live volume → snapshot → backup → lvremove. Degraded RAID → replace member → wait full rebuild.

---

## Quick Assessment Checklist

1. [ ] PV/VG/LV map captured (pvs/vgs/lvs)?
2. [ ] RAID under it healthy (/proc/mdstat)?
3. [ ] Free space at the right layer?
4. [ ] fs resize step included for extends?
5. [ ] Rollback point (snapshot or backup) considered?

---

## Expected Output Format

### Volume Map
[Before/after PV/VG/LV + RAID state]

### Changes
[Exact commands, sizes, backups]

### Verification
[lvs + df -h post-change; mdstat if RAID]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| df unchanged after extend | fs not resized | resize2fs/xfs_growfs |
| Mirror won't create | Only 2 PVs | -m 1 needs 3 PVs (log lives on third) |
| Snapshot invalid | Snap% hit 100 | lvremove broken snap; recreate larger |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| (none) | Local shell execution via agent (lvm/mdadm) | — | — |

No external MCP bindings: LVM/RAID state comes from local tools. Unavailable data is NOT AVAILABLE, never fabricated.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|-------------------|
| devops-surveyor | Always first | pvs/vgs/lvs/mdstat evidence |
| devops-analyst | Capacity incidents | Where growth must come from |
| devops-operator | Approved changes | Extend/migrate/snapshot with verification |

---

## Related Skills

- **storage-filesystems**: Partitioning and fstab beneath the LVM layer
- **backup-restore**: Backing up snapshots; dd images of members
- **resource-monitoring**: I/O pressure from storage layers

---

## Questions to Ask

1. Which volume/md array, and what outcome (size, consistency, health)?
2. Is there VG free, or must new storage join the group?
3. Any maintenance-window constraint (online vs umount)?
