#!/usr/bin/env python3

grid = []
positions = []
with open('input.txt') as infile:
    lines = infile.readlines()
    for y, line in enumerate(lines):
        grid.append([c for c in line.strip()]) 
        if 'S' in line:
            positions.append((y, line.index('S')))

def show_grid(grid, positions):
    for y, row in enumerate(grid):
        line = '' 
        for x, col in enumerate(row):
            if (y, x) in positions:
                line += 'O'
            else:
                line += grid[y][x]
        print(line)

def free(pos):
    return pos[0] >= 0 and pos[0] < len(grid) and pos[1] >= 0 and \
        pos[1] < len(grid[0]) and grid[pos[0]][pos[1]] in ['.', 'S']

for _ in range(64):
    new_positions = []
    for p in positions:
        south = (p[0] + 1, p[1])
        if free(south) and not south in new_positions:
            new_positions.append(south)
        west = (p[0], p[1] - 1)
        if free(west) and not west in new_positions:
            new_positions.append(west)
        north = (p[0] - 1, p[1])
        if free(north) and not north in new_positions:
            new_positions.append(north)
        east = (p[0], p[1] + 1)
        if free(east) and not east in new_positions:
            new_positions.append(east)
    positions = new_positions

# show_grid(grid, positions)
print(len(positions))
