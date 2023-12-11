#!/usr/bin/env python3

with open('input.txt') as infile:
    lines = infile.readlines()

universe = []
for line in lines:
    patches = [c for c in line.strip()]
    universe.append(patches)
    if len([c for c in patches if c != '.']) == 0:
        universe.append(patches)

columns = []
for x_idx in range(0, len(universe[0])):
    all_empty = True
    for y_idx in range(0, len(universe)):
        if universe[y_idx][x_idx] != '.':
            all_empty = False
            break
    if all_empty:
        columns.append(x_idx)
for row in universe:
    for idx, col in enumerate(columns):
       row.insert(col + idx, '.')

locations = []
for y_idx, row in enumerate(universe):
    for x_idx, col in enumerate(row):
        if col == '#':
            locations.append((x_idx, y_idx))

pairs = []
for idx, loc in enumerate(locations):
    for i in range(idx + 1, len(locations)):
        pairs.append((loc, locations[i]))

total = 0
for p in pairs:
    distance = abs(p[0][0] - p[1][0]) + abs(p[0][1] - p[1][1])
    total += distance
print(total)    
