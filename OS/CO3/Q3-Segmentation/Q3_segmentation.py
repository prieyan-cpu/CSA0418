"""
Q3 - Segmentation: segment-table translation with base and limit checks.
"""
# Each entry is (base address, limit). Limit is the segment length in bytes.
segment_table = {
    0: (1000, 400),
    1: (5000, 1200),
    2: (9000, 800),
    3: (12000, 600),
}

def translate(segment, offset):
    if segment not in segment_table:
        return "invalid segment"
    base, limit = segment_table[segment]
    if offset < 0 or offset >= limit:
        return "segmentation fault: offset exceeds segment limit"
    return base + offset

tests = [(0, 0), (0, 399), (0, 400), (1, 250), (1, 1199),
         (2, 800), (3, 55), (4, 10)]
for seg, off in tests:
    print(f"(segment={seg}, offset={off}) -> {translate(seg, off)}")

print("\nPure paging: fixed-size pages; no external fragmentation, but some internal waste.")
print("Pure segmentation: logical variable-size segments; external fragmentation can occur.")
print("Segmented paging: each segment is divided into pages, combining logical segments with paging.")
print("Linux memory mappings can be inspected with: cat /proc/<PID>/maps")
