#!/usr/bin/env python3

with open('input-small.txt') as infile:
    lines = infile.readlines()

grid = []
for line in lines:
    grid.append([c for c in line.strip()])

def trace(beam, grid, visited):
    x = beam[1]
    y = beam[0]
    direction = beam[2]
    while True:
        if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
            return []
        tile = grid[y][x]
        if (y, x, direction) in visited:
            return []
        else: 
            visited.append((y, x, direction))
        if tile == '|':
            if direction == 'left' or direction == 'right':
                return [(y - 1, x, 'up'), (y + 1, x, 'down')] 
        elif tile == '-':
            if direction == 'up' or direction == 'down':
                return [(y, x - 1, 'left'), (y, x + 1, 'right')]
        elif tile == '\\':
            if direction == 'up':
                return [(y, x - 1, 'left')]
            elif direction == 'down':
                return [(y, x + 1, 'right')]
            if direction == 'right':
                return [(y + 1, x, 'down')]
            elif direction == 'left':
                return [(y - 1, x, 'up')]
        elif tile == '/':
            if direction == 'up':
                return [(y, x + 1, 'right')]
            elif direction == 'down':
                return [(y, x - 1, 'left')]
            if direction == 'right':
                return [(y - 1, x, 'up')]
            elif direction == 'left':
                return [(y + 1, x, 'down')]
        if direction == 'right':
            x += 1
        elif direction == 'left':
            x -= 1
        elif direction == 'up':
            y -= 1
        elif direction == 'down':
            y += 1

def calc_energized(start, grid):
    beams = [start]
    visited = []
    while beams:
        beams.extend(trace(beams.pop(), grid, visited))
    visited = set([(v[0], v[1]) for v in visited])
    result = len(visited)
    print(f'{start} = {result}')
    return result

start_coords = []
start_coords.extend([(0, x, 'down') for x in range(len(grid[0]))])
start_coords.extend([(y, len(grid[0]) - 1, 'left') for y in range(len(grid))])
start_coords.extend([(len(grid) - 1, x, 'up') for x in range(len(grid[0]))])
start_coords.extend([(y, 0, 'right') for y in range(len(grid))])

print(max([calc_energized(s, grid) for s in start_coords]))
