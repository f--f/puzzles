"""Advent of Code 2019 Day 2: 1202 Program Alarm"""

import helper
import itertools

def run_program(intcode):
    OPS = {1: int.__add__, 2: int.__mul__}
    i = 0  # index of current opcode
    opcode = intcode[i]
    while opcode != 99:
        assert opcode in (1, 2, 99)
        operation = OPS[opcode]
        intcode[intcode[i+3]] = operation(intcode[intcode[i+1]], 
                                          intcode[intcode[i+2]])
        i += 4
        opcode = intcode[i]
    return intcode


def run_program_with_inputs(intcode, noun, verb):
    memory = intcode.copy()
    memory[1] = noun
    memory[2] = verb
    return run_program(memory)


assert tuple(run_program([1,0,0,0,99])) == (2,0,0,0,99)
assert tuple(run_program([2,3,0,3,99])) == (2,3,0,6,99)
assert tuple(run_program([2,4,4,5,99,0])) == (2,4,4,5,99,9801)
assert tuple(run_program([1,1,1,4,99,5,6,0,99])) == (30,1,1,4,2,5,6,0,99)

# part 1
input_data = [int(n) for n in helper.read_day(2).split(",")]
# replace position 1 with value 12 and 2 with value 2 as requested

print(run_program_with_inputs(input_data, 12, 2)[0])

# part 2
for noun, verb in itertools.product(range(100), range(100)):
    output = run_program_with_inputs(input_data, noun, verb)[0]
    if output == 19690720:
        print("Found gravity assist input:", 100*noun + verb)