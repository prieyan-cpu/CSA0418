"""
Q5 - FIFO, LRU and Optimal page-replacement algorithms.
"""
def fifo(ref, frames):
    memory, faults, pointer = [], 0, 0
    for page in ref:
        if page in memory:
            continue
        faults += 1
        if len(memory) < frames:
            memory.append(page)
        else:
            memory[pointer] = page
            pointer = (pointer + 1) % frames
    return faults

def lru(ref, frames):
    memory, last_used, faults = [], {}, 0
    for i, page in enumerate(ref):
        if page in memory:
            last_used[page] = i
            continue
        faults += 1
        if len(memory) < frames:
            memory.append(page)
        else:
            victim = min(memory, key=lambda p: last_used[p])
            memory[memory.index(victim)] = page
            del last_used[victim]
        last_used[page] = i
    return faults

def optimal(ref, frames):
    memory, faults = [], 0
    for i, page in enumerate(ref):
        if page in memory:
            continue
        faults += 1
        if len(memory) < frames:
            memory.append(page)
            continue
        future = ref[i+1:]
        def next_use(p):
            return future.index(p) if p in future else float("inf")
        victim = max(memory, key=next_use)
        memory[memory.index(victim)] = page
    return faults

if __name__ == "__main__":
    reference = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    for f in (3, 4):
        print(f"{f} frames: FIFO {fifo(reference,f)}, LRU {lru(reference,f)}, Optimal {optimal(reference,f)}")
    belady = [1,2,3,4,1,2,5,1,2,3,4,5]
    print("Belady string, FIFO:", fifo(belady,3), "faults with 3 frames;",
          fifo(belady,4), "faults with 4 frames")
