"""Advent of Code 2017 Day 2: Corruption Checksum"""

def parse(text):
    """Convert spreadsheet text input to nested list of integers."""
    return [list(map(int, line.split())) for line in text.splitlines()]


def checksum(sheet):
    """Given rows of random numbers in text format, calculate the checksum,
    which is the sum of differences between the largest and smallest value
    for each row.
    """
    diffs = (max(row) - min(row) for row in sheet)
    return sum(diffs)


def evenly_divisible_checksum(sheet):
    """Compute checksum summing division of evenly divisible numbers.

    Approach:
    - Compute all pairs of numbers in each row 
    - For each set of pairs, check evenly divisible and if so compute result
    - Sort numbers so that we know which should be the numerator
    """
    divs = []
    for row in sheet:
        row = sorted(row)
        pairs = [(u, v) for u in row for v in row if u < v]
        divs.append([v//u for u, v in pairs if v % u == 0][0])
    return sum(divs)


p1_ex = """5 1 9 5
7 5 3
2 4 6 8
"""
assert checksum(parse(p1_ex)) == 18

p2_ex = """5 9 2 8
9 4 7 3
3 8 6 5
"""
assert evenly_divisible_checksum(parse(p2_ex)) == 9