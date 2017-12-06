"""Advent of Code 2017 Day 6: Memory Reallocation""" 

import helper

def count_cycles(banks):
    """Returns number of cycles needed and length of cycle."""
    banks = banks.copy()
    N = len(banks)
    prev_configs = []  # Store previous cycle configurations
    count = 0

    while banks not in prev_configs:
        prev_configs.append(banks.copy())

        # Redistribute the blocks:
        # Get max value and its index (prioritizing lowest index first)
        # Note banks.index(max(banks)) works, but this needs to traverse twice
        idx, blocks = max([(i,v) for i,v in enumerate(banks)],
                          key=lambda k: (k[1], N-k[0]))
        banks[idx] = 0
        for i in range(1, blocks+1):
            banks[(idx+i) % N] += 1
        count += 1
    return(count, count-prev_configs.index(banks))

assert count_cycles([0,2,7,0]) == (5, 4)

banks_input = list(map(int, helper.read_day(6).split()))
output = count_cycles(banks_input)
print("{} cycles completed with infinite loop length of {}.".format(*output))