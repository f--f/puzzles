"""Advent of Code Day 11: Hex Ed"""

import helper

"""
You can traverse a hex grid entirely using only two vectors (let's say North
and North-East). We can represent all 6 directions as combinations of these:
    n = 1*n
    s = -1*n
    ne = 1*ne
    sw = -1*ne
    nw = 1*n - 1*ne
    se = -1*n + 1*ne
To find distance, note that the following "simplifications" exist:
    n - ne (2 steps) = nw (1 step)
    -n + ne (2 steps) = sw (1 step)
    n + ne (2 steps), can't be reduced
meaning distance can be represented as: max(abs(n), abs(ne), abs(n+ne))
"""

def steps_away(dirs):
    """Compute shortest number of steps away based on steps taken so far."""
    n = dirs["n"] - dirs["s"] + dirs["nw"] - dirs["se"]
    ne = dirs["ne"] - dirs["sw"] - dirs["nw"] + dirs["se"]
    return(max(abs(n), abs(ne), abs(n+ne)))

def hex_steps(path):
    """Count number of steps to return to origin given directions (part 1) 
    and furthest number of steps (part 2)."""
    furthest = 0
    dirs = {"n":0,"nw":0,"ne":0,"sw":0,"s":0,"se":0}
    for step in path:
        dirs[step] += 1
        if steps_away(dirs) > furthest:
            furthest = steps_away(dirs)
    return(steps_away(dirs), furthest)

# Test Part 1
assert hex_steps(["ne","ne","ne"])[0] == 3
assert hex_steps(["ne","ne","sw","sw"])[0] == 0
assert hex_steps(["ne","ne","s","s"])[0] == 2
assert hex_steps(["se","sw","se","sw","sw"])[0] == 3

data = helper.read_day(11).strip().split(',')
print(hex_steps(data))