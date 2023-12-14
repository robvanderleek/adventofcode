#!/usr/bin/env python3
import math
import sys

sys.setrecursionlimit(14000)

with open('input-small5.txt') as infile:
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
        result = walk(next_pos, trail + [next_pos])
        if result:
            return result
    next_pos = (pos[0] + 1, pos[1])
    if can_go_south(pos):
        result = walk(next_pos, trail + [next_pos])
        if result:
            return result
    next_pos = (pos[0], pos[1] - 1)
    if can_go_west(pos):
        result = walk(next_pos, trail + [next_pos])
        if result:
            return result
    next_pos = (pos[0] - 1, pos[1])
    if can_go_north(pos):
        result = walk(next_pos, trail + [next_pos])
        if result:
            return result
    return None

trail = walk(start, [])
print(math.floor(len(trail) / 2))

enclosed = 0
for idx_y, row in enumerate(grid):
    in_loop = False
    in_l = False
    in_f = False
    for idx_x, col in enumerate(grid[idx_y]):
        if (idx_y, idx_x) in trail:
            if in_f:
                if col == 'J':
                    in_loop = not in_loop
                    in_f = False
                elif col == '7':
                    in_f = False
            if in_l:
                if col == '7':
                    in_loop = not in_loop
                    in_l = False
                elif col == 'J':
                    in_l = False
            elif col in ['|']:
                in_loop = not in_loop
            elif col == 'L':
                in_l = True
            elif col == 'F' or col == 'S':
                in_f = True
        else:
            if in_loop:
                print((idx_y, idx_x))
                enclosed += 1
    if in_loop:
        print('OOPS')    
        print(idx_y)
print(enclosed)

