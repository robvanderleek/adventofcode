#!/usr/bin/env python3

with open('input.txt') as infile:
    lines = infile.readlines()
    plan = []
    for line in lines:
        parts = line.strip().split(' ')
        plan.append((parts[0], int(parts[1])))

def dim(plan):
    xmin = ymin = 0
    xmax = ymax = 0
    pos = [0, 0]
    for d in plan:
        if d[0] == 'R':
            pos[0] += d[1]
        elif d[0] == 'D':
            pos[1] += d[1] 
        elif d[0] == 'L':
            pos[0] -= d[1]
        elif d[0] == 'U':
            pos[1] -= d[1] 
        xmin = min(xmin, pos[0])
        ymin = min(ymin, pos[1])
        xmax = max(xmax, pos[0])
        ymax = max(ymax, pos[1])
    return ((xmax - xmin) + 1, (ymax - ymin) + 1), xmin, ymin 

def shoelace(verts):
    totalX = 0
    totalY = 0
    for idx, v in enumerate(verts[:-1]):
        totalX += v[0] * verts[idx + 1][1] 
        totalY += v[1] * verts[idx + 1][0] 
    totalX += verts[-1][0] * verts[0][1] 
    totalY += verts[-1][1] * verts[0][0] 
    return abs(totalX - totalY) / 2

def show(grid):
    for line in grid:
        print(''.join(line))

dimensions = dim(plan)
grid = []
for y in range(dimensions[0][1]):
    grid.append(['.' for x in range(dimensions[0][0])])

pos = [0, 0]
verts = [(0, 0)]
for d in plan:
    if d[0] == 'R':
        for _ in range(d[1]):
            pos[0] += 1
            grid[pos[1]][pos[0]] = '#'
        verts.append((pos[0], pos[1]))
    if d[0] == 'D':
        for _ in range(d[1]):
            pos[1] += 1
            grid[pos[1]][pos[0]] = '#'
        verts.append((pos[0], pos[1]))
    if d[0] == 'L':
        for _ in range(d[1]):
            pos[0] -= 1
            grid[pos[1]][pos[0]] = '#'
        verts.append((pos[0], pos[1]))
    if d[0] == 'U':
        for _ in range(d[1]):
            pos[1] -= 1
            grid[pos[1]][pos[0]] = '#'
        verts.append((pos[0], pos[1]))

show(grid)

trench = sum([d[1] for d in plan])
print((shoelace(verts[:-1]) + (trench / 2)) + 1)
