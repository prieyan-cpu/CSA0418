"""
Q2 - Paging: logical-to-physical address translation and page-table calculations.
"""
PAGE_SIZE = 1024
PAGES = 8
page_table = [5, 2, -1, 7, 0, -1, 3, -1]
logical_addresses = [0, 1500, 3100, 6200, 9000, 2049]

def translate(address, page_size=PAGE_SIZE, table=page_table):
    page = address // page_size
    offset = address % page_size
    if page >= len(table):
        return page, offset, "invalid address"
    frame = table[page]
    if frame == -1:
        return page, offset, "page fault"
    return page, offset, frame * page_size + offset

print("Logical address translation (page size =", PAGE_SIZE, ")")
for address in logical_addresses:
    page, offset, result = translate(address)
    if isinstance(result, int):
        print(f"{address:5} -> page {page} offset {offset:6} : physical {result}")
    else:
        print(f"{address:5} -> page {page} offset {offset:6} : {result}")

print("\nPage table entries for 32-bit address space, 4 KB pages:",
      (2**32 // 4096), "entries")
print("Page table entries for 48-bit address space, 4 KB pages:",
      (2**48 // 4096), "entries (single-level, impractically large)")

# Simple EAT example: TLB lookup 10 ns, memory access 100 ns, hit ratio 95%.
tlb, mem, hit = 10, 100, 0.95
eat = hit * (tlb + mem) + (1-hit) * (tlb + 2*mem)
print(f"Example TLB effective access time (95% hit): {eat:.1f} ns")

# Recalculate with the assignment's requested 2 KB page size.
print("\nWith page size 2048:")
for address in logical_addresses:
    page, offset, result = translate(address, page_size=2048)
    print(address, "->", "page", page, "offset", offset, "result", result)
