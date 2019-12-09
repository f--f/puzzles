"""Advent of Code 2019 Day 4: Secure Container"""

from collections import Counter


def is_valid_part1(num):
    strnum = str(num)
    is_ordered = ''.join(sorted(strnum)) == strnum
    has_dupes = len(set(strnum)) != 6
    # note has_dupes doesn't explicitly check for adjacent digits, but it doesn't matter
    # since the password needs to be ordered as well
    # could avoid has_dupes since AND short circuits, but less descriptive...
    return is_ordered and has_dupes


def is_valid_part2(num):
    # at least one pair of adjacent matching digits
    return is_valid_part1(num) and (2 in Counter(str(num)).values())


def count_valid(vrange, valid_func):
    valid_count = 0
    for num in range(*vrange):
        if valid_func(num):
            valid_count += 1
    return valid_count


assert is_valid_part1(111111)
assert not is_valid_part1(223450)
assert not is_valid_part1(123789)

pw_range = (172930, 683083)
print("Part 1:", count_valid(pw_range, is_valid_part1))

assert is_valid_part2(112233)
assert not is_valid_part2(123444)
assert is_valid_part2(111122)

print("Part 2:", count_valid(pw_range, is_valid_part2))
