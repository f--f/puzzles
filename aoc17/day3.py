"""Advent of Code 2017 Day 3: Spiral Memory"""

def get_size(num):
    """Returns 'size' of spiral corresponding to where the number is located.
    ex. Any number in 2 to 9 will return 3, since it corresponds to the
    "3x3"-sized layer.

    Approach: The bottom right corners of the grid form a pattern of odd
    squares, which can be represented by a series (2n-1)^2. We can invert
    the identified square to get the size.
    """
    return 2*int(((num-1)**0.5 + 1) / 2) + 1


def dist(num):
    """Returns the steps required to carry the data from an identified square.

    Approach: Given size n (n^2 corresponds to the bottom right corner), we
    know that the maximum distance to 1 is at each corner, where the number of
    steps is (n-1). Then, for each distance away from the closest corner, we
    reduce the distance by that many steps.
    """
    if num == 1: return 0  # Handle base case
    n = get_size(num)
    max_dist = n-1
    for corner in range(n**2, (n-2)**2, -(n-1)):
        steps_from_corner = abs(corner - num)
        if steps_from_corner < n//2+1:  # Closest corner to num
            return max_dist - steps_from_corner


def sum_neighbours(d,x,y):
    """Given a coordinate (x,y) and a dict d with keys of coordinates,
    return sum of neighbours of (x,y). (Undefined coordinates count as 0.)
    """
    return sum(d.get((i,j),0) for i in range(x-1,x+2) 
                              for j in range(y-1,y+2) 
                              if not (i == x and j == y))


def spiral_stress(num):
    """Find first value in spiral that is larger than num.

    Approach: Brute-force, spiral outwards, manually creating a dictionary
    mapping each coordinate to its value and stopping when you read a number
    greater than num.
    """
    x, y = 0, 0
    spiral = {(x,y): 1}
    while True:
        x += 1  # move right once onto next "layer"
        spiral[(x,y)] = sum_neighbours(spiral,x,y)
        # generate move increments in x, y to trace the spiral
        xmove = [0]*(2*x-1) + [-1]*(2*x) + [0]*(2*x) + [1]*(2*x)
        ymove = [1]*(2*x-1) + [0]*(2*x) + [-1]*(2*x) + [0]*(2*x)
        for xi, yi in zip(xmove, ymove):
            x += xi  # move
            y += yi
            spiral[(x,y)] = sum_neighbours(spiral,x,y)
            if spiral[(x,y)] > num:
                return spiral[(x,y)]

# Part 1     
assert dist(1) == 0
assert dist(12) == 3
assert dist(23) == 2
assert dist(1024) == 31

# Part 2 (test cases based on the part of the spiral given)
assert spiral_stress(305) == 330
assert spiral_stress(1) == 2
assert spiral_stress(747) == 806