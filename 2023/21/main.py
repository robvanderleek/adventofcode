#!/usr/bin/env python3

grid = []
with open('input.txt') as infile:
    lines = infile.readlines()
    for y, line in enumerate(lines):
        grid.append([c for c in line.strip()]) 
        if 'S' in line:
            S = (y, line.index('S'))

free_positions = set()
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if col == '.' or col == 'S':
            free_positions.add((y, x))

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
   return (pos[0] % len(grid), pos[1] % len(grid[0])) in free_positions

def calc(n):
    positions = [S]
    for _ in range(n):
        new_positions = set()
        for p in positions:
            south = (p[0] + 1, p[1])
            if free(south) and not south in new_positions:
                new_positions.add(south)
            west = (p[0], p[1] - 1)
            if free(west) and not west in new_positions:
                new_positions.add(west)
            north = (p[0] - 1, p[1])
            if free(north) and not north in new_positions:
                new_positions.add(north)
            east = (p[0], p[1] + 1)
            if free(east) and not east in new_positions:
                new_positions.add(east)
        positions = new_positions
    return len(positions)

r1 = calc(65)
r2 = calc(65 + 131)
r3 = calc(65 + 2 * 131)
a = (r3 + r1 - (2 * r2)) / 2
b = ((4 * r2) - (3 * r1) - r3) / 2
c = r1
print((a * pow(202300, 2)) + (b * 202300) + c)
