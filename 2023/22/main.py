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

def get_brick(x, y, z, bricks):
    z_bricks = [b for b in bricks if b[0][2] <= z and b[1][2] >= z]
    y_bricks = [b for b in z_bricks if b[0][1] <= y and b[1][1] >= y]
    x_bricks = [b for b in y_bricks if b[0][0] <= x and b[1][0] >= x]
    return x_bricks[0] if x_bricks else None

def get_lower_bricks(brick, bricks):
    (_, _, z) = brick[0]
    if z == 1:
        return set(brick)
    return get_level_bricks(brick, bricks, z - 1)

def get_higher_bricks(brick, bricks):
    (_, _, z) = brick[1]
    return get_level_bricks(brick, bricks, z + 1)

def get_level_bricks(brick, bricks, level):
    (x1, y1, _) = brick[0]
    (x2, y2, _) = brick[1]
    result = [] 
    for x in range(min(x1, x2), max(x1, x2) + 1):
        b = get_brick(x, y1, level, bricks)
        if b:
            result.append(b)
    for y in range(min(y1, y2), max(y1, y2) + 1):
        b = get_brick(x1, y, level, bricks)
        if b:
            result.append(b)
    return set(result)

def do_fall(bricks):
    result = []
    for b in bricks:
        (x1, y1, z1) = b[0]
        (x2, y2, z2) = b[1]
        while len(get_lower_bricks(((x1, y1, z1), (x2, y2, z2)), result)) == 0:
            z1 -= 1
            z2 -= 1
        result.append(((x1, y1, z1), (x2, y2, z2)))
    return result

def can_be_disintegrated(brick, bricks):
    higher = get_higher_bricks(brick, bricks) 
    for h in higher:
        if len(get_lower_bricks(h, bricks)) < 2:
            return False
    return True

def count_fall(removed, all_removed, bricks):
    result = 0
    higher = set()
    for r in removed:
        higher.update(get_higher_bricks(r, bricks))
    if higher:
        higher_that_would_fall = []
        for h in higher:
            lower = get_lower_bricks(h, bricks)
            if lower.issubset(all_removed):
                result += 1
                higher_that_would_fall.append(h) 
        all_removed.update(higher_that_would_fall)
        result += count_fall(higher_that_would_fall, all_removed, bricks)
    return result

print('Waiting for bricks to fall...')
fixed_bricks = do_fall(bricks) 
print('Done!')

total = 0
can_be_removed = 0
for b in fixed_bricks:
    if can_be_disintegrated(b, fixed_bricks):
        can_be_removed += 1
    else:
        s = set()
        s.add(b)
        total += count_fall(s, s, fixed_bricks)
print(f'Can be removed: {can_be_removed}')
print(f'Would fall: {total}')
