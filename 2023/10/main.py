#!/usr/bin/env python3
import math
import sys

sys.setrecursionlimit(14000)

with open('input.txt') as infile:
    lines = infile.readlines()
grid = []
S = None
for idx, line in enumerate(lines):
    line_pipes = [c for c in line.strip()]
    grid.append(line_pipes)
    if 'S' in line_pipes:
        S = (idx, line_pipes.index('S'))

def get_pipe(y, x):
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
        return None
    return grid[y][x]
    
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
    if get_pipe(pos[0], pos[1]) in ['-', 'L', 'F', 'S'] and \
            get_pipe(pos[0], pos[1] + 1) in ['-', 'J', '7', 'S']:
        result = walk(next_pos, trail + [next_pos])
        if result:
            return result
    next_pos = (pos[0] + 1, pos[1])
    if get_pipe(pos[0], pos[1]) in ['|', '7', 'F', 'S'] and \
            get_pipe(pos[0] + 1, pos[1]) in ['|', 'L', 'J', 'S']:
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

trail = walk(S, [])
print(math.floor(len(trail) / 2))

def replace_S(grid, trail):
    after = trail[0]
    before = trail[-2]
    if before[0] > S[0] and before[1] == S[1] and after[0] == S[0] and after[1] > S[1]:
        grid[S[0]][S[1]] = 'F'
    elif before[0] < S[0] and before[1] == S[1] and after[0] == S[0] and after[1] > S[1]:
        grid[S[0]][S[1]] = 'L'
    elif before[0] == S[0] and before[1] < S[1] and fter[0] > S[0] and after[1] == S[1]:
        grid[S[0]][S[1]] = '7'
    elif before[0] < S[0] and before[1] == S[1] and after[0] == S[0] and after[1] < S[1]:
        grid[S[0]][S[1]] = 'J'
    else:
        grid[S[0]][S[1]] = '|'

replace_S(grid, trail)

enclosed = 0
for idx_y, row in enumerate(grid):
    in_loop = in_l = in_f = False
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
            elif col == 'F':
                in_f = True
        else:
            if in_loop:
                enclosed += 1

print(enclosed)
