#!/usr/bin/env python3

def load_universe():
    with open('input.txt') as infile:
        lines = infile.readlines()
    result = []
    for line in lines:
        patches = [c for c in line.strip()]
        result.append(patches)
    return result

def get_empty_rows(universe):
    result = []
    for idx, row in enumerate(universe):
        if len([c for c in row if c != '.']) == 0:
            result.append(idx)
    return result

def get_empty_columns(universe):
    result = []
    for x_idx in range(0, len(universe[0])):
        all_empty = True
        for y_idx in range(0, len(universe)):
            if universe[y_idx][x_idx] != '.':
                all_empty = False
                break
        if all_empty:
            result.append(x_idx)
    return result 

def load_galaxies(universe):
    result = []
    for y_idx, row in enumerate(universe):
        for x_idx, col in enumerate(row):
            if col == '#':
                result.append((x_idx, y_idx))
    return result

def expand(galaxies, empty_rows, empty_columns, factor):
    result = []
    for g in galaxies:
        new_x = g[0] + (len([c for c in empty_columns if c < g[0]]) * (factor - 1))
        new_y = g[1] + (len([r for r in empty_rows if r < g[1]]) * (factor - 1))
        result.append((new_x, new_y))
    return result

universe = load_universe()
empty_rows = get_empty_rows(universe)
empty_columns = get_empty_columns(universe)
galaxies = load_galaxies(universe)
galaxies = expand(galaxies, empty_rows, empty_columns, 1000000)

pairs = []
for idx, loc in enumerate(galaxies):
    for i in range(idx + 1, len(galaxies)):
        pairs.append((loc, galaxies[i]))

total = 0
for p in pairs:
    distance = abs(p[0][0] - p[1][0]) + abs(p[0][1] - p[1][1])
    total += distance
print(total)    
