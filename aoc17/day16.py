"""Advent of Code Day 16: Permutation Promenade"""
 
import helper

# Part 1

def dance(progs, moves):
    """Return program order from dancing with moves."""
    progs = list(progs)
    for move in moves:
        if move[0] == "s":  # Spin
            spin = int(move[1:])
            progs = progs[-spin:] + progs[:-spin]
        elif move[0] == "x":  # Exchange
            a, b = map(int, move[1:].split("/"))
            progs[a], progs[b] = progs[b], progs[a]
        elif move[0] == "p":  # Partner
            a, b = move[1:].split("/")
            ia, ib = progs.index(a), progs.index(b)
            progs[ia], progs[ib] = progs[ib], progs[ia]
    return ''.join(progs)

assert dance("abcde", ["s1", "x3/4", "pe/b"]) == "baedc"

progs = "abcdefghijklmnop"
moves = helper.read_day(16).strip().split(",")
progs = dance(progs, moves)
print("Part 1:", progs)

# Part 2

# We can't brute-force a billion answers: let's try to instead find
# a recurring cycle.
# Initialize list of "solutions" with part 1 answer.
solutions = [progs]
for i in range(1,1000000000):
    progs = dance(progs, moves)
    if progs in solutions:
        solutions.append(progs)
        break
    else:
        solutions.append(progs)

cycle_length = (len(solutions)-1) - solutions.index(solutions[-1])
# Note we're zero-index, need the solution for the "999999999th"-idx dance
print("Part 2:", solutions[:-1][(1000000000-1) % cycle_length])