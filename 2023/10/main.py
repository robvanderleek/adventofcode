#!/usr/bin/env python3
import math

with open('input-small.txt') as infile:
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

def come_from(trail, direction):
    reverse = {'west': 'east', 'north': 'south', 'east': 'west',
               'south': 'north'}
    if trail:
        return trail[-1] == reverse[direction]
    else:
        return False

def walk(pos, trail):
    if grid[pos[0]][pos[1]] == 'S' and len(trail) > 0:
        return trail
    if can_go_east(pos) and not come_from(trail, 'east'):
        result = walk((pos[0], pos[1] + 1), trail + ['east'])
        if result:
            return result
    if can_go_south(pos) and not come_from(trail, 'south'):
        result = walk((pos[0] + 1, pos[1]), trail + ['south'])
        if result:
            return result
    if can_go_west(pos) and not come_from(trail, 'west'):
        result = walk((pos[0], pos[1] - 1), trail + ['west'])
        if result:
            return result
    if can_go_north(pos) and not come_from(trail, 'north'):
        result = walk((pos[0] - 1, pos[1]), trail + ['north'])
        if result:
            return result
    return None

distance = len(walk(start, []))
print(math.floor(distance / 2))
