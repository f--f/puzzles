"""Advent of Code Day 13: Packet Scanners"""

import helper

def parse_firewall(inp):
    """Parse input file to firewall data (dictionary)."""
    firewall = {}
    inp = inp.splitlines()
    for layer in inp:
        depth, rng = map(int, layer.split(": "))
        firewall[depth] = rng
    return firewall

# Part 1
# Simulate packet stepping through firewall.

firewall = parse_firewall(helper.read_day(13).strip())
severity = 0
time = 0
for step in range(max(firewall)+1):
    # Get caught if:  time % ((firewall[step]-1)*2) == 0 where
    # (firewall[step]-1)*2 is the number of moves to complete one cycle of
    # going down and up the range of a layer. Equals 0 since we are travelling
    # on the tops of each layer.
    if step in firewall and time % ((firewall[step]-1)*2) == 0:
        severity += step*firewall[step]
    time += 1

print(severity)

# Part 2 
# Brute-force this by restarting the simulation with increased delay each time 
# we are caught, until we succeed.

delay = 0
caught = True
while caught:
    time = delay
    caught = False
    for step in range(max(firewall)+1):
        caught = step in firewall and time % ((firewall[step]-1)*2) == 0
        if caught:
            delay += 1
            break
        time += 1

print(delay)