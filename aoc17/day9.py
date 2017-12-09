"""Advent of Cody Day 9: Stream Processing"""

import helper

def score(stream):
    """Score a stream. Returns total score (part 1) and non-cancelled
    characters (part 2)."""
    score = 0
    depth = 0
    count_garbage = 0  # Part 2
    in_garbage = False
    cancelled = False
    for c in stream:
        # Ignore cancelled characters
        if cancelled: 
            cancelled = False
            continue
        if in_garbage:
            if c == ">":
                in_garbage = False
            elif c == "!":
                cancelled = True
            else:
                count_garbage += 1
        else:
            if c == "{":  # Open group
                depth += 1
                score += depth
            elif c == "}":  # Close group
                depth -= 1
            elif c == "<":
                in_garbage = True
    return(score, count_garbage)


# Test Part 1
assert score("{}")[0] == 1
assert score("{{{}}}")[0] == 6
assert score("{{},{}}")[0] == 5
assert score("{<a>,<a>,<a>,<a>}")[0] == 1
assert score("{{<ab>},{<ab>},{<ab>},{<ab>}}")[0] == 9
assert score("{{<a!>},{<a!>},{<a!>},{<ab>}}")[0] == 3

# Test Part 2
assert score("<>")[1] == 0
assert score("<random characters>")[1] == 17
assert score("<<<<>")[1] == 3
assert score("<!!!>>")[1] == 0
assert score("""<{o"i!a,<{i<a>""")[1] == 10

stream = helper.read_day(9).strip()
print(score(stream))