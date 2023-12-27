#!/usr/bin/env python3

bricks = []
with open('input.txt') as infile:
    lines = infile.readlines()
    for line in lines:
        parts = line.strip().split('~')
        end1 = tuple(int(i) for i in parts[0].split(','))
        end2 = tuple(int(i) for i in parts[1].split(','))
        if end1[2] <= end2[2]:
            bricks.append((end1, end2))
        else:
            bricks.append((end2, end1))
bricks.sort(key=lambda b: b[0][2])

def get_block(x, y, z, bricks):
    z_bricks = [b for b in bricks if b[0][2] <= z and b[1][2] >= z]
    y_bricks = [b for b in z_bricks if b[0][1] <= y and b[1][1] >= y]
    x_bricks = [b for b in y_bricks if b[0][0] <= x and b[1][0] >= x]
    return x_bricks[0] if x_bricks else None

def get_lower_blocks(brick, bricks):
    (_, _, z) = brick[0]
    if z == 1:
        return set(brick)
    return get_level_bricks(brick, bricks, z - 1)

def get_higher_blocks(brick, bricks):
    (_, _, z) = brick[1]
    return get_level_bricks(brick, bricks, z + 1)

def get_level_bricks(brick, bricks, level):
    (x1, y1, _) = brick[0]
    (x2, y2, _) = brick[1]
    result = [] 
    for x in range(min(x1, x2), max(x1, x2) + 1):
        b = get_block(x, y1, level, bricks)
        if b:
            result.append(b)
    for y in range(min(y1, y2), max(y1, y2) + 1):
        b = get_block(x1, y, level, bricks)
        if b:
            result.append(b)
    return set(result)

fixed_bricks = []
for b in bricks:
    (x1, y1, z1) = b[0]
    (x2, y2, z2) = b[1]
    while len(get_lower_blocks(((x1, y1, z1), (x2, y2, z2)), fixed_bricks)) == 0:
        z1 -= 1
        z2 -= 1
    fixed_bricks.append(((x1, y1, z1), (x2, y2, z2)))

def can_be_disintegrated(brick, bricks):
    higher = get_higher_blocks(brick, bricks)
    for h in higher:
        if len(get_lower_blocks(h, bricks)) < 2:
            return False
    return True
    
total = 0
for b in fixed_bricks:
    if can_be_disintegrated(b, fixed_bricks):
        total += 1
print(total)
