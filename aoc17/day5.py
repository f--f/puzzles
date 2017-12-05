"""Advent of Code 2017 Day 2: A Maze of Twisty Trampolines, All Alike""" 

import helper

def jump(jumps, offset):
    """Given jump array and offset function, compute number of jumps."""
    jumps = jumps.copy()  # Copy to avoid modifying list
    idx = 0  # current location
    prev = 0  # previous location
    count = 0  # number of jumps so far
    while not (idx >= len(jumps) or idx < 0):
        prev = idx
        idx += jumps[idx]  # Jump to new position
        count += 1
        jumps[prev] += offset(jumps[prev])  # Shift previous position
    return count

# Offset functions for part 1 & 2
offset_p1 = lambda offset: 1
offset_p2 = lambda offset: -1 if offset >= 3 else 1

assert jump([0,3,0,1,-3], offset_p1) == 5
assert jump([0,3,0,1,-3], offset_p2) == 10

# Try for actual input
input_data = list(map(int, helper.read_day(5).splitlines()))
print("Part 1:", jump(input_data, offset_p1))
print("Part 2:", jump(input_data, offset_p2))
