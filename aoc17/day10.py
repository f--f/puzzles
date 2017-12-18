import helper
import itertools

def reverse_cycle(lst, start, end):
    """Reverses part of a circular list in-place.
    Ex: [0,1,2,(3,4][0,1),2,3,4] -> [...2,(1,0][4,3),2...]"""
    N = len(lst)
    # Select the part of the cycle to reverse
    group = itertools.islice(itertools.cycle(lst[:]), start, end)
    # Reverse group by writing into the list in reverse index order
    for i in reversed(range(start, end)):
        lst[i % N] = next(group)

# def reverse_cycle(lst, s, e):
#     """Alternative solution using swapping (but maybe less intuitive?)."""
#     N = len(lst)
#     for i in range((e-s)//2):
#         lst[(s+i)%N], lst[(e-i-1)%N] = lst[(e-i-1)%N], lst[(s+i)%N]

def hash_round(lst, lengths, curr=0, skip=0):
    """Return hashed list after one round."""
    lst = lst.copy()
    N = len(lst)
    for l in lengths:
        reverse_cycle(lst, curr, curr+l)
        curr = (curr + l + skip) % N
        skip += 1
    return (lst, curr, skip)


def knot_hash(input_string):
    """Returns knot hash given an input string (lengths)."""
    # Read lengths as ASCII characters
    lst = list(range(0,256))
    lengths = [ord(ch) for ch in input_string]
    lengths += [17, 31, 73, 47, 23]
    curr, skip = 0, 0
    for i in range(64):
        lst, curr, skip = hash_round(lst, lengths, curr, skip)
    # Get dense hash by taking blocks of numbers
    dense = []
    for i in range(16):
        xor = 0
        for j in range(16):
            xor ^= lst[i*16+j]
        dense.append(xor)
    # Convert 16 numbers to hex string
    knothash = ''.join([hex(num)[2:].zfill(2) for num in dense])
    return(knothash)

assert hash_round([0,1,2,3,4], [3,4,1,5])[0][0:2] == [3,4]

assert knot_hash("") == "a2582a3a0e66e6e86e3812dcb672a272"
assert knot_hash("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
assert knot_hash("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
assert knot_hash("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"

if __name__ == "__main__":  # Need to re-use the functions on day 14

    lst = list(range(0,256))
    lengths = list(map(int, helper.read_day(10).strip().split(',')))
    part1 = hash_round(lst, lengths)[0]
    print("Part 1 solution:", part1[0]*part1[1])
    
    input_string = helper.read_day(10).strip()
    print("Part 2 solution:", knot_hash(input_string))