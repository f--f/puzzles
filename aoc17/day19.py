"""Advent of Code Day 19: A Series of Tubes"""
 
import helper
import numpy as np

input_data = helper.read_day(19)

def traverse_diagram(input_data):
    # Convert data to a numpy grid (easier to index into)
    grid = np.array([list(line) for line in input_data.splitlines()])

    curr = '|'  # Start from '|' on first line
    row, col = 0, np.where(grid[0,:] == '|')[0][0]
    face = 'S'  # Compass direction
    path = []
    steps = 0

    while True:
        steps += 1
        if face == 'S': row += 1
        elif face == 'N': row -= 1
        elif face == 'W': col -= 1
        elif face == 'E': col += 1
        curr = grid[row, col]

        if curr == '+':
            # Which direction to turn into? Check non-empty adjacent cells.
            if face == 'N' or face == 'S':
                face = 'E' if grid[row, col+1] != ' ' else 'W'
            elif face == 'E' or face == 'W':
                face = 'S' if grid[row+1, col] != ' ' else 'N'
        elif curr.isalpha(): path.append(curr)
        elif curr == ' ':
            break  # Exited the grid.
    return ''.join(path), steps


# Check example case
test_case = """     |          
     |  +--+    
     A  |  C    
 F---|--|-E---+ 
     |  |  |  D 
     +B-+  +--+ 
                
"""
assert traverse_diagram(test_case)[0] == "ABCDEF"
assert traverse_diagram(test_case)[1] == 38

solution = traverse_diagram(input_data)
print("Part 1:", solution[0])
print("Part 2:", solution[1])