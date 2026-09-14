# Doddle DevOps OS

Linux server administration skills for DoddleOS — validated graph blueprints
(SKILL.md + blueprint.yaml) covering the full operational surface of a Linux
server: processes, storage, LVM/RAID, boot and services, scheduling and
logging, resource monitoring, package management, networking/SSH, kernel
modules, and backup/restore.

## Skills

| Skill | ID | Covers |
|-------|----|--------|
| `process-management` | `doddle.devops.process` | ps/top/pgrep, signals (HUP/TERM/KILL/STOP/CONT), nice/renice, jobs/fg/bg |
| `storage-filesystems` | `doddle.devops.storage` | disk discovery, partitions (fdisk/parted, MBR/GPT), mkfs/tune2fs/fsck, mount/fstab/UUID, secure mount options |
| `lvm-raid` | `doddle.devops.lvm` | RAID levels + mdadm, LVM pv/vg/lv lifecycle, online extend, mirrors, snapshots, pvmove, iSCSI/multipath overview |
| `boot-and-services` | `doddle.devops.boot` | boot sequence, grub/grub2, kernel parameters, init/runlevels legacy, systemd systemctl/targets/journal |
| `scheduling-and-logging` | `doddle.devops.scheduling` | at/atq/atrm, crontab syntax, /etc/cron.*, login logging (who/last/lastb), rsyslog, logger, logrotate |
| `resource-monitoring` | `doddle.devops.monitoring` | /proc/meminfo, free truth, swap management, vmstat/iostat/iotop/mpstat/sar, lsof/fuser forensics |
| `package-management` | `doddle.devops.packages` | dpkg/apt-get/aptitude, rpm/yum, repositories, verifying files, building from source |
| `networking-ssh` | `doddle.devops.networking` | ip/ifconfig, Debian/RHEL nic config, route/arp/ping, bonding, ssh/scp/key setup, tcpdump, NFS, iptables |
| `kernel-modules` | `doddle.devops.kernel` | uname//proc/cmdline, /boot files, lsmod/modprobe/depmod, module deps, ldd/ltrace/strace |
| `backup-restore` | `doddle.devops.backup` | gzip/bzip2, tar workflows incl. ssh pipes, dump/restore levels, cpio+find, dd images, split |

## Agents

| Agent | Role |
|-------|------|
| `devops-surveyor` | Read-only evidence collection; establishes system state before any hypothesis |
| `devops-analyst` | Root-cause analysis from evidence; severity grading |
| `devops-operator` | Change execution with approval gating, one-variable-at-a-time, verify-after-repair |

## Safety model

Every repair-class blueprint carries a `gate` node (approvers, timeout) before
its apply step: mutating commands are proposed first, approved by the owner,
then executed and verified. Read-only surveying never needs approval. One
variable changes at a time; every repair is verified against the original
symptom.

## Validation

```bash
python3 ../../doddle-core/scripts/validate.py   # 0 errors target
```

## Attribution

Skill content is derived from **Linux System Administration** by Paul Cobbaut
(linux-training.be, 2015), distributed under the GNU Free Documentation License
1.3. The derived skill texts in this pack follow that license; the pack
scaffolding is MIT like the rest of DoddleOS.
