""" 
Arrays: containers which hold multiple data records and are addressable 
by index (random access). Arrays occupy contiguous blocks in memory.

Properties (given n values):
- Space complexity: O(n)
- Time complexity:
    - O(1) access - just need index to access the value in memory
    - O(1) insertion at the end of the array
    - O(n) insertion at the beginning (requires every element to be shifted)

In Python, dynamically sized arrays are implemented via lists.

This short script uses the timeit module to demonstrate the time scaling of
these operations on dynamic arrays (lists).
"""

import timeit
import random

N = 100 # Number of executions to timeit.

class ArrayTiming():
    def __init__(self, n):
        self.a = [0]*n
        self.random_index = random.randint(0,len(self.a))
    def insert_beginning(self):
        self.a.insert(0,1)
    def insert_end(self):
        self.a.append(1)
    def access(self):
        self.a[self.random_index]

a_small = ArrayTiming(1000)
a_large = ArrayTiming(10000)

# Note: code below here could be reused for other data structures.

times = {
    "access": [0,0],
    "ins_begin": [0,0],
    "ins_end": [0,0]
}

for i, a in enumerate([a_small, a_large]):
    # Compare access:
    times["access"][i] = timeit.Timer(a.access).timeit(N)

    # Insertion at beginning:
    times["ins_begin"][i] = timeit.Timer(a.insert_beginning).timeit(N)

    # Insertion at end:
    times["ins_end"][i] = timeit.Timer(a.insert_end).timeit(N)

time_ratio = lambda t: t[1] / t[0]
print(time_ratio(times["access"]))
print(time_ratio(times["ins_begin"])) # Much slower as list size increases!
print(time_ratio(times["ins_end"]))