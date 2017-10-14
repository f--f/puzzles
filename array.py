""" 
Arrays: containers which hold multiple data records and are addressable 
by index (random access). Arrays occupy contiguous blocks in memory.

Properties (given n values):
- Space complexity: O(n)
- Time complexity:
    - O(1) access - just need index to access the value in memory
- For dynamic arrays:
    - O(1) insertion at the end of the array
    - O(n) insertion at the beginning (requires every element to be shifted)
- There is a worst-case O(n) cost for insertion if the array's capacity needs 
to be expanded, but the amortized cost is O(1).

In Python, dynamically sized arrays are implemented via lists.

This short script uses the timeit module to demonstrate the time scaling of
these operations on dynamic arrays (lists).
"""

from matplotlib import pyplot as plt
import timeit
import random

class ArrayTiming():
    def __init__(self, n):
        self.a = [0]*n
        self.random_index = random.randint(0,len(self.a)-1)
    def insert_beginning(self):
        self.a.insert(0,1)
    def insert_end(self):
        self.a.append(1)
    def access(self):
        self.a[self.random_index]

N = 10000 # Number of executions to timeit.
samples = [1000*(i)+1 for i in range(10)]
arrs = [ArrayTiming(n) for n in samples]

times = {
    "access": [0]*len(samples),
    "ins_begin": [0]*len(samples),
    "ins_end": [0]*len(samples),
}

for i, a in enumerate(arrs):
    # Compare access:
    times["access"][i] = timeit.Timer(a.access).timeit(N)
    # Insertion at beginning:
    times["ins_begin"][i] = timeit.Timer(a.insert_beginning).timeit(N)
    # Insertion at end:
    times["ins_end"][i] = timeit.Timer(a.insert_end).timeit(N)

# Plot time as N increases to demonstrate scaling
for key, val in times.items():
    plt.plot(samples, val, 'o', label=key)
plt.title("time complexity of array operations")
plt.xlabel('n')
plt.ylabel('time')
plt.legend(loc='best')
plt.show()