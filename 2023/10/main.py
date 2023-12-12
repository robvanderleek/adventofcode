#!/usr/bin/env python3
import math
import sys

sys.setrecursionlimit(14000)

with open('input.txt') as infile:
    lines = infile.readlines()
grid = []
start = None
for idx, line in enumerate(lines):
    line_pipes = [c for c in line.strip()]
    grid.append(line_pipes)
    if 'S' in line_pipes:
        start = (idx, line_pipes.index('S'))

def get_pipe(y, x):
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
        return None
    return grid[y][x]
    
def can_go_east(pos):
    return get_pipe(pos[0], pos[1]) in ['-', 'L', 'F', 'S'] and \
        get_pipe(pos[0], pos[1] + 1) in ['-', 'J', '7', 'S']

def can_go_south(pos):
    return get_pipe(pos[0], pos[1]) in ['|', '7', 'F', 'S'] and \
        get_pipe(pos[0] + 1, pos[1]) in ['|', 'L', 'J', 'S']

def can_go_west(pos):
    return get_pipe(pos[0], pos[1]) in ['-', 'J', '7', 'S'] and \
        get_pipe(pos[0], pos[1] - 1) in ['-', 'L', 'F', 'S']

def can_go_north(pos):
    return get_pipe(pos[0], pos[1]) in ['|', 'L', 'J', 'S'] and \
        get_pipe(pos[0] - 1, pos[1]) in ['|', '7', 'F', 'S']

visited = []

def walk(pos, trail):
    if pos in visited:
        if grid[pos[0]][pos[1]] == 'S' and len(trail) > 2:
            return trail
        else:
            return None
    else:
        visited.append(pos)
    next_pos = (pos[0], pos[1] + 1)
    if can_go_east(pos):
        result = walk(next_pos, trail + ['east'])
        if result:
            return result
    next_pos = (pos[0] + 1, pos[1])
    if can_go_south(pos):
        result = walk(next_pos, trail + ['south'])
        if result:
            return result
    next_pos = (pos[0], pos[1] - 1)
    if can_go_west(pos):
        result = walk(next_pos, trail + ['west'])
        if result:
            return result
    next_pos = (pos[0] - 1, pos[1])
    if can_go_north(pos):
        result = walk(next_pos, trail + ['north'])
        if result:
            return result
    return None

print(math.floor(len(walk(start, [])) / 2))
