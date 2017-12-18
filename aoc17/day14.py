"""Advent of Code Day 14: Disk Defragmentation"""

from day10 import knot_hash
import numpy as np

key = "hwlqcszp"
grid = np.zeros((128,128), dtype=int)

# Part 1
# Each knot hash (128 bits) corresponds to a single row in the 128x128 grid
for row in range(128):
    inp = key + "-" + str(row)  # Input to knot hash
    out = knot_hash(inp)
    # Convert hex digit to padded binary
    grid[row,:] = list(''.join([bin(int(digit, base=16)).lstrip("0b").zfill(4) 
                                for digit in out]))
print("Number of squares used:", grid.sum())

# Part 2
def map_region(i, j, label):
    """Map out region: recursively search neighbours until we reach
    a neighbour without any neighbours.""" 
    grid[i,j] = label
    for l, m in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
        if 0 <= l <= 127 and 0 <= m <= 127: # Ignore out-of-bounds/wrapping
            if grid[l, m] == 1:
                map_region(l, m, label)

regions = 0
for i in range(128):
    for j in range(128):
        if grid[i,j] == 1: # Find unlabelled regions (1-values)
            map_region(i, j, 2+regions) # Index new regions starting from 2
            regions += 1
print("Number of regions:", regions)