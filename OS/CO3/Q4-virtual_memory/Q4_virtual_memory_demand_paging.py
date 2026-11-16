"""
Q4 - Virtual memory and demand paging.
Simulates page faults for sequential and random page-reference patterns.
"""
import random

def count_faults(references, frames):
    resident = set()
    faults = 0
    # FIFO replacement for a compact illustrative simulation.
    queue = []
    for page in references:
        if page not in resident:
            faults += 1
            if len(queue) == frames:
                old = queue.pop(0)
                resident.remove(old)
            queue.append(page)
            resident.add(page)
    return faults

def effective_access_time(memory_ns, fault_rate, fault_service_ms):
    # Convert page-fault service time from ms to ns.
    service_ns = fault_service_ms * 1_000_000
    return (1 - fault_rate) * memory_ns + fault_rate * (service_ns + memory_ns)

if __name__ == "__main__":
    n = 10000
    sequential = [i % 128 for i in range(n)]
    random.seed(7)
    random_refs = [random.randrange(128) for _ in range(n)]
    print("Page faults with 16 frames:")
    print("Sequential:", count_faults(sequential, 16))
    print("Random:    ", count_faults(random_refs, 16))

    print("\nEffective access time (memory=100 ns, fault service=8 ms):")
    for rate in (1/1000, 1/100000, 1/1000000):
        print(f"fault rate {rate:.8f}: {effective_access_time(100, rate, 8):,.2f} ns")

    print("\nCopy-on-write: fork() initially shares physical pages; a write causes a private copy.")
    print("Thrashing: the system spends excessive time servicing page faults rather than executing.")
