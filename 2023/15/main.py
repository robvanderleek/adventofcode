#!/usr/bin/env python3
import re

with open('input.txt') as infile:
    lines = infile.readlines()
parts = lines[0].strip().split(',')

def calc_hash(l):
    result = 0
    for c in l:
        result += ord(c)
        result = result * 17
        result = result % 256
    return result

boxes = []
for _ in range(256):
    boxes.append([])

for p in parts:
    label = re.split('[=-]', p)[0]
    box = calc_hash(label)
    if p[-1] == '-':
        boxes[box] = [b for b in boxes[box] if not b.startswith(label)]
    else:
        focal_length = p[-1]
        for idx, lens in enumerate(boxes[box]):
            if lens.startswith(label):
                boxes[box][idx] = f'{label} {focal_length}'
                break
        else:
            boxes[box].append(f'{label} {focal_length}')

total = 0
for idx_b, b in enumerate(boxes):
    for idx_l, lens in enumerate(b):
        total += (idx_b + 1) * (idx_l + 1) * int(lens[-1])
print(total)
