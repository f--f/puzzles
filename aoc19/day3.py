"""Advent of Code 2019 Day 3: Crossed Wires"""

import helper


def manhattan(p):
    return abs(p[0]) + abs(p[1])


def get_points_on_wire_path(wire):
    """w is a list of path commands"""
    points = set()
    points_to_lowest_steps = {}
    x, y = 0, 0  # current position
    n = 0  # step count
    for path in wire:
        move, dist = path[0], int(path[1:])
        for step in range(dist):
            if move == "R":   x += 1
            elif move == "L": x -= 1
            elif move == "U": y += 1
            elif move == "D": y -= 1
            n += 1
            points.add((x, y))
            if (x, y) not in points_to_lowest_steps:  # only track fewest steps to reach
                points_to_lowest_steps[(x, y)] = n
    return points, points_to_lowest_steps


def get_closest_and_nearest_intersections(w1, w2):
    """
    w1 and w2 are each a string containing the wire paths.
    approach:
    - keep track of every point along the path for each wire
    - find set of points that intersect w1 and w2
    - calculate manhatten distance for each and return lowest
    """
    w1, w1_lowest_steps = get_points_on_wire_path(w1.split(","))
    w2, w2_lowest_steps = get_points_on_wire_path(w2.split(","))
    intersections = w1.intersection(w2)
    intersections.discard((0,0))  # ignore output port
    # Part 1: sort all intersection points by Manhattan distance and return lowest
    closest_point = sorted(intersections, key=manhattan)[0]
    # Part 2: sort by lowest combined step count
    fewest_steps_point = sorted(intersections, 
                   key=lambda p: w1_lowest_steps[p] + w2_lowest_steps[p])[0]

    return (manhattan(closest_point),
            w1_lowest_steps[fewest_steps_point] + w2_lowest_steps[fewest_steps_point])


assert get_closest_and_nearest_intersections(
    "R75,D30,R83,U83,L12,D49,R71,U7,L72",
    "U62,R66,U55,R34,D71,R55,D58,R83") == (159, 610)

assert get_closest_and_nearest_intersections(
    "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
    "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7") == (135, 410)

input_wires = helper.read_day(3).splitlines()
output = get_closest_and_nearest_intersections(*input_wires)
print("Part 1:", output[0])
print("Part 2:", output[1])