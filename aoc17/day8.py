"""Advent of Code 2017 Day 8: I Heard You Like Registers""" 

import helper 
from collections import defaultdict

def process_registers(instructs):
    """Processes register instructions. Returns tuple consisting of largest
    value in a register after completion (part 1) and highest value held at
    any point in time in a register (part 2)."""
    registers = defaultdict(int)  # Default to zero
    highest = 0
    OPS = {"inc": "+=", "dec": "-="}

    for line in instructs:
        key, op, opval, *cond = line.split()
        # Build an expression like "a += 1 if b >= 2 else 0"
        # (Pass registers into local namespace for expression)
        expr = [key, OPS[op], opval] + cond + ["else 0"]
        exec(' '.join(expr), None, registers)
        # Part 2 - Query highest value
        highest = max(registers[key], highest)
    return(max(registers.values()), highest)

# Test Part 1 & 2
assert process_registers("""b inc 5 if a > 1
                            a inc 1 if b < 5
                            c dec -10 if a >= 1
                            c inc -20 if c == 10""".splitlines()) == (1,10)

instructs = helper.read_day(8).splitlines()
print(process_registers(instructs))