"""Advent of Code Day 21: Fractal Art"""
 
import helper
import numpy as np

def pattern_to_grid(string):
    return np.array([list(row) for row in string.split('/')])

def grid_to_pattern(grid):
    return '/'.join([''.join(row) for row in grid.tolist()])

def split_grid(grid):
    """Split grid pattern into 2x2 or 3x3, returning subpatterns."""
    size = grid.shape[0]
    # Prioritize 2x2 rules over 3x3 unless size is odd
    split = 2 if size % 2 == 0 else 3
    subs = []
    for i in range(0, size, split):
        for j in range(0, size, split):
            subs.append(grid[i:i+split, j:j+split])
    return subs

def connect_grids(subs):
    """Connects subgrids into larger grid."""
    # Output size
    if len(subs) == 1:
        return subs[0]
    dim = int(len(subs)**(0.5))
    split = subs[0].shape[0]
    grid = np.empty((dim*split,dim*split), dtype='<U1')
    for i in range(dim):
        for j in range(dim):
            grid[i*split:(i+1)*split, j*split:(j+1)*split] = subs[(i*dim)+j]
    return grid

def enumerate_patterns(grid):
    """Given a base grid pattern, enumerates over the rest of the patterns 
    attainable by flip/rotates and returns the set."""
    pat_set = set()
    tmp = grid[:,:]
    for rot in range(4):
        tmp = tmp.T[:,::-1]  # 90deg rotation
        pat_set.add(grid_to_pattern(tmp[:,:]))
        # Horizontal and vertical flips
        pat_set.add(grid_to_pattern(tmp[::-1,:]))
        pat_set.add(grid_to_pattern(tmp[:,::-1]))
    return pat_set

# Parse enhancement guide
input_file = helper.read_day(21).strip().splitlines()
guide = {}
for line in input_file:
    inp, out = line.split(' => ')
    # Consider all rotations / flips in input
    equivs = enumerate_patterns(pattern_to_grid(inp))
    for pat in equivs:
        guide[pat] = out

# Enhance loop
grid = pattern_to_grid(".#./..#/###")
pixels_on = []
for step in range(18):
    # Split grid into subgrids
    out_subs = []
    for sub in split_grid(grid):
        # Match subgrid to enhancement guide
        out_subs.append(pattern_to_grid(guide[grid_to_pattern(sub)]))
    # Collect subgrids into single grid
    grid = connect_grids(out_subs)
    pixels_on.append(np.sum(grid == '#'))

print("Part 1:", pixels_on[4])
print("Part 2:", pixels_on[17])