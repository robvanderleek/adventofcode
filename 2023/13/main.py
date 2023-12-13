#!/usr/bin/env python3
from copy import deepcopy

with open('input.txt') as infile:
    lines = [line.strip() for line in infile.readlines()]

patterns = []
cur_pattern = []
for line in lines:
    if line == '':
        patterns.append(cur_pattern)
        cur_pattern = []
    else:
        cur_pattern.append([c for c in line])
patterns.append(cur_pattern)

def find_vertical(p, exclude = None):
    for idx in range(1, len(p[0])):
        length = min(idx, len(p[0]) - idx)
        left = []
        for col in range(idx - length, idx):
            left.append(''.join([row[col] for row in p])) 
        right = []
        for col in range(idx, idx + length):
            right.append(''.join([row[col] for row in p]))
        if left == right[::-1] and idx != exclude:
            return idx
    return None

def find_horizontal(p, exclude = None):
    for idx in range(1, len(p)):
        length = min(idx, len(p) - idx)
        up = p[idx - length:idx]
        down = p[idx:idx + length]
        if up == down[::-1] and idx != exclude:
            return idx
    return None

def fix_smudge(p):
    result = []
    for idx_y in range(len(p)):
        for idx_x in range(len(p[0])):
            p_copy = deepcopy(p)
            cur = p_copy[idx_y][idx_x]
            if cur == '.':
                p_copy[idx_y][idx_x] = '#'
            else:
                p_copy[idx_y][idx_x] = '.'
            result.append(p_copy)
    return result

def find_reflection(p, exclude=None):
    n = find_vertical(p) if not exclude or exclude >= 100 \
        else find_vertical(p, exclude)
    if n:
        return n
    else:
        n = find_horizontal(p) if not exclude or exclude < 100 else \
            find_horizontal(p, exclude / 100) 
        if n:
            return n * 100

total = 0
for p in patterns:
    ref_p = find_reflection(p)
    fixed = fix_smudge(p)
    for f in fixed:
        ref_f = find_reflection(f, ref_p)
        if ref_f:
            total += ref_f
            break
print(total)
