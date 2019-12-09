"""Advent of Code 2019 Day 5: Sunny with a Chance of Asteroids"""

import helper
import itertools

OPS = {
    # Key is the opcode value
    # Value is a 3-tuple consisting of:
    # - the operation to perform
    # - the number of 'input' parameters
    # - the number of 'output' (write) parameters
    # The operation will be performed on the inputs and written to the outputs
    # (currently the number of outputs is only 0 or 1)
    1: (int.__add__, 2, 1),
    2: (int.__mul__, 2, 1),
    3: (lambda: int(input("Enter input: ")), 0, 1),
    4: (lambda p: print(f"Output: {p}"), 1, 0),
    # 5/6 need access to the instruction pointer which I didn't foresee so they're
    # kind of hacked in right now
    5: (None, 2, 0),
    6: (None, 2, 0),

    7: (lambda *p: int(p[0] < p[1]), 2, 1),
    8: (lambda *p: int(p[0] == p[1]), 2, 1),
}

def extract_opcode(command):
    return int(str(command)[-2:])

def run_program(intcode):
    i = 0  # index of current opcode

    while True:  # halt=99
        opcode = extract_opcode(intcode[i])
        assert opcode in OPS.keys() or opcode == 99
        if opcode == 99: break

        n = OPS[opcode][1]  # number of non-write parameters
        m = OPS[opcode][2]  # number of write parameters (always immediate mode)
        modes = [int(m) for m in reversed(str(intcode[i]).zfill(2 + n)[:-2])]
        operation = OPS[opcode][0]
        params = [
            intcode[intcode[i+j+1]] if modes[j] == 0 else intcode[i+j+1]
            for j in range(n)
        ]
        # ~~ special cases ~~
        if opcode == 5 or opcode == 6:
            if opcode == 5:
                if params[0] != 0: 
                    i = params[1]
                    continue
            elif opcode == 6:
                if params[0] == 0:
                    i = params[1]
                    continue
        # ~~ end special cases ~~
        else:
            if m == 1:  # write
                intcode[intcode[i+n+m]] = operation(*params)
            elif m == 0:
                operation(*params)
        i += n + m + 1
    return intcode


assert extract_opcode(1002) == 2
assert extract_opcode(1001) == 1


# same tests from day 2 (should be backwards compatible)
assert tuple(run_program([1,0,0,0,99])) == (2,0,0,0,99)
assert tuple(run_program([2,3,0,3,99])) == (2,3,0,6,99)
assert tuple(run_program([2,4,4,5,99,0])) == (2,4,4,5,99,9801)
assert tuple(run_program([1,1,1,4,99,5,6,0,99])) == (30,1,1,4,2,5,6,0,99)

input_data = [int(n) for n in helper.read_day(5).split(",")]
run_program(input_data)