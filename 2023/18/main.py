#!/usr/bin/env python3

with open('input.txt') as infile:
    lines = infile.readlines()
    plan = []
    for line in lines:
        parts = line.strip().split(' ')
        hex = parts[2][2:-1]
        dir = 'R' if hex[-1] == '0' else 'D' if hex[-1] == '1' else 'L' \
            if hex[-1] == '2' else 'U'
        plan.append((dir, int(hex[:-1], 16)))

def shoelace(verts):
    totalX = 0
    totalY = 0
    for idx, v in enumerate(verts[:-1]):
        totalX += v[0] * verts[idx + 1][1] 
        totalY += v[1] * verts[idx + 1][0] 
    totalX += verts[-1][0] * verts[0][1] 
    totalY += verts[-1][1] * verts[0][0] 
    return abs(totalX - totalY) / 2

def to_verts(plan):
    pos = [0, 0]
    verts = [(0, 0)]
    for d in plan:
        if d[0] == 'R':
            pos[0] += d[1]
            verts.append((pos[0], pos[1]))
        if d[0] == 'D':
            pos[1] += d[1]
            verts.append((pos[0], pos[1]))
        if d[0] == 'L':
            pos[0] -= d[1]
            verts.append((pos[0], pos[1]))
        if d[0] == 'U':
            pos[1] -= d[1]
            verts.append((pos[0], pos[1]))
    return verts

verts = to_verts(plan)
trench = sum([d[1] for d in plan])
print((shoelace(verts[:-1]) + (trench / 2)) + 1)
