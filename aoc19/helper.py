"""Helper functions for Advent of Code 2017"""

def read_day(day):
    """Read input file for the day, returning a string."""
    filename = "inputs/{}.txt".format(day)
    with open(filename, 'r') as f:
        output = f.read()
    return output