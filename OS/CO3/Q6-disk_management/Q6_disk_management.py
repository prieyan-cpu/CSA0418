"""
Q6 - Disk management: RAID usable capacity and simplified reliability estimates.
Assumes six equal 4 TB disks and decimal TB units.
"""
DISKS = 6
DISK_TB = 4
annual_disk_failure_probability = 0.02  # illustrative assumption, not a vendor guarantee

raid_capacity = {
    "RAID 0": DISKS * DISK_TB,
    "RAID 1 (six-way mirror)": DISK_TB,
    "RAID 5": (DISKS - 1) * DISK_TB,
    "RAID 6": (DISKS - 2) * DISK_TB,
    "RAID 10": (DISKS // 2) * DISK_TB,
}
print("Usable capacity for six 4 TB disks:")
for raid, capacity in raid_capacity.items():
    print(f"{raid:24s}: {capacity} TB")

p = annual_disk_failure_probability
# Simplified independent-failure approximation over one year.
# RAID 5 loses data if at least two disks fail before a rebuild completes;
# this annual approximation ignores rebuild windows and correlated failures.
prob_two_or_more = 1 - (1-p)**DISKS - DISKS*p*(1-p)**(DISKS-1)
prob_three_or_more = sum(
    __import__("math").comb(DISKS, k) * p**k * (1-p)**(DISKS-k)
    for k in range(3, DISKS+1)
)
print(f"\nIllustrative probability of >=2 disk failures in one year: {prob_two_or_more:.6%}")
print(f"Illustrative probability of >=3 disk failures in one year: {prob_three_or_more:.6%}")
print("RAID 1 (mirroring): redundancy depends on mirror layout; this script's six-way mirror")
print("survives up to five disk failures if at least one copy remains.")
print("Inspect Linux storage with: lsblk ; sudo fdisk -l ; swapon --show")
