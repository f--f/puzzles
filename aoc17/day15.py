"""Advent of Code Day 15: Dueling Generators"""

from itertools import islice

# Part 1
# Initialize both generators

def genA(val):
    while True:
        val = (val * 16807) % 2147483647
        yield val

def genB(val):
    while True:
        val = (val * 48271) % 2147483647
        yield val

# Explanation of finding whether the last 16 bits match:
# a ^ b returns 0s where the bits match
# & 65535 returns 0 if the last 16 bits are zero, since
# 65535 = 0000 0000 0000 0000 1111 1111 1111 1111

judge_count = sum(1 for a, b in islice(zip(genA(703), genB(516)), 40000000) 
                  if not (a ^ b) & 65535)

print("Part 1:", judge_count)

# Part 2
# Let's modify our generator functions to only yield on multiples.

def genA(val):
    while True:
        val = (val * 16807) % 2147483647
        if val % 4 == 0:
            yield val

def genB(val):
    while True:
        val = (val * 48271) % 2147483647
        if val % 8 == 0:
            yield val

# This doesn't change, apart from truncating the generator to 5M values.
judge_count = sum(1 for a, b in islice(zip(genA(703), genB(516)), 5000000)
                  if not (a ^ b) & 65535)

print("Part 2:", judge_count)