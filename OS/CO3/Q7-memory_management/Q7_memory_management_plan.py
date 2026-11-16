"""
Q7 - Memory-management plan for a 2 GB smart-factory edge device.
Illustrative capacity accounting in MiB; change assumptions to match measurements.
"""
TOTAL_RAM = 2048
REAL_TIME = 256
ML_TASK = 1536
LOGGING = 128
OS_AND_RESERVE = 128

tasks = {
    "Real-time control (locked)": REAL_TIME,
    "Machine-learning task": ML_TASK,
    "Logging task": LOGGING,
    "OS and safety reserve": OS_AND_RESERVE,
}
used = sum(tasks.values())
print("Memory plan (MiB):")
for name, amount in tasks.items():
    print(f"{name:32s}: {amount:4d} MiB")
print(f"Total allocated: {used} MiB / {TOTAL_RAM} MiB")
print(f"Remaining headroom: {TOTAL_RAM-used} MiB")

extra_task = 500
print(f"\nIf a fourth 500 MiB task is added: required={used+extra_task} MiB")
if used + extra_task > TOTAL_RAM:
    print("Over capacity: reject, reduce the ML working set, or upgrade device memory.")
else:
    print("The additional task fits within the assumed RAM budget.")

print("\nLinux implementation concept:")
print("1. Allocate and prefault the real-time task's memory before control starts.")
print("2. Use mlock()/mlockall() where permitted; check return values and resource limits.")
print("3. Avoid dynamic allocation and blocking I/O in the real-time control loop.")
print("4. Reserve memory for the OS and verify worst-case latency under load.")
print("5. A hard real-time RTOS with static allocation can provide more predictable timing.")
