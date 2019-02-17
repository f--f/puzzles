"""Advent of Code Day 18: Duet"""
 
import helper
import re
from collections import defaultdict, deque

input_data = helper.read_day(18).strip().splitlines()

# Part 1

def map_value(registers, val):
    """Maps an argument in an instruction to a numeric value.
    Letters are converted to the values in their register, while numbers are
    treated normally (as integers)."""
    return int(val) if re.match("[a-z]", val) is None else int(registers[val])

def parse_instruction(registers, instruction, args, line_num):
    """Parses a line of the instructions, excluding snd/rcv (special cases).
    Returns a line number (to deal with jumps)."""
    # First argument is a register, second is a value
    ch = args[0]
    val = map_value(registers, args[1])
    if instruction == "set":
        registers[ch] = val
    elif instruction == "add":
        registers[ch] += val
    elif instruction == "mul":
        registers[ch] *= val
    elif instruction == "mod":
        registers[ch] %= val
    elif instruction == "jgz":
        if map_value(registers, ch) > 0:
            line_num += val - 1
    return line_num

registers = defaultdict(int)  # each register starts with value of 0
last_sound = None
line_num = 0  # Line number of current instruction
while line_num < len(input_data):
    # Parse instruction
    instruction, *args = input_data[line_num].split()
    if len(args) == 2:
        line_num = parse_instruction(registers, instruction, args, line_num)
    else:  # snd/rcv
        ch = args[0]
        if instruction == "snd":
            last_sound = map_value(registers, ch)
        elif instruction == "rcv":
            if registers[ch] != 0:
                registers[ch] = last_sound
                break
    line_num += 1

print("Part 1:", last_sound)

# Part 2
# Let's do this serially, with control switching between program 0 and 
# program 1 whenever one is forced to wait for a send.

# Initialize program states
progs = []
for i in range(2):
    progs.append({
            'registers': defaultdict(int),
            'send_queue': deque(),
            'line_num': 0,
            'waiting': False,
            })
progs[1]['registers']['p'] = 1  # Special case for Program 1
curr = 0                        # ID of current program
prog1_count = 0                 # Part 2 solution

# Run while not deadlocked
while not all(prog['waiting'] for prog in progs):
    registers = progs[curr]['registers']
    line_num = progs[curr]['line_num']

    # Parse instruction
    instruction, *args = input_data[line_num].split()
    if len(args) == 2:
        progs[curr]['line_num'] = parse_instruction(registers, instruction, 
                                                    args, line_num)
    else:  # snd/rcv
        ch = args[0]
        if instruction == "snd":
            progs[curr]['send_queue'].append(map_value(registers, ch))
            progs[not curr]['waiting'] = False  # Cancel a wait upon new send
            if curr == 1:
                prog1_count += 1
        elif instruction == "rcv":
            if progs[not curr]['send_queue']:
                # Other program's send queue is not empty
                registers[ch] = progs[not curr]['send_queue'].popleft()
            else:
                # Can't perform the receive
                progs[curr]['waiting'] = True
                progs[curr]['line_num'] -= 1
    progs[curr]['line_num'] += 1
    if progs[curr]['waiting']:
        curr = int(not curr)  # Switch control to other program

print("Part 2:", prog1_count)
