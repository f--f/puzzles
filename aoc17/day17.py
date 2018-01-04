"""Advent of Code Day 17: Spinlock"""

buff = [0]  # circular buffer
pos = 0    # position
inp = 382

for val in range(1,2018):
    pos = (pos + inp) % len(buff) + 1
    buff.insert(pos, val)

print("Part 1:", buff[buff.index(2017)+1])

# Part 2:
# Key info is that we want the value after 0, and the location of 0 is fixed
# since we're always inserting to the right.
# So let's ignore inserting the other values! Just keep track of when we
# decide to "insert" after the zero (at index 1):

pos = 0
val_after_zero = 0
for length in range(1,50000001):
    pos = (pos + inp) % length + 1
    if pos == 1:
        val_after_zero = length

print("Part 2:", val_after_zero)