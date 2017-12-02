"""Advent of Code 2017 Day 1: Inverse Captcha"""

def sum_next(num):
    """
    Find sum of all digits in num that match the next digit in the list of
    numbers. The list is circular (digit after last is the first).
    
    Approach:
    - Loop over digits and compare each digit with the next, if same then
      include digit in sum.
    """
    digits = str(num)  # So we can iterate over digits.
    N = len(digits)
    return sum(int(curr) for i, curr in enumerate(digits)
               if curr == digits[(i+1) % N])


def sum_halfway(num):
    """
    Extend Part 1 by summing all digits that match the digit halfway around the
    list. Assume the number of digits in the list is even.

    Approach:
    - Same as Part 1, but compare with the number that is i+N/2 numbers ahead.
    """
    digits = str(num)
    N = len(digits)
    return sum(int(curr) for i, curr in enumerate(digits)
               if curr == digits[(i+N//2) % N])

# Test Part 1
assert sum_next(1122) == 3
assert sum_next(1111) == 4
assert sum_next(1234) == 0
assert sum_next(91212129) == 9

# Test Part 2
assert sum_halfway(1212) == 6
assert sum_halfway(1221) == 0
assert sum_halfway(123425) == 4
assert sum_halfway(123123) == 12
assert sum_halfway(12131415) == 4