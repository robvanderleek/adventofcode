#!/usr/bin/env python3
import re

rows = []

with open('input-small.txt') as infile:
    lines = infile.readlines()
    for line in lines:
        parts = line.strip().split(' ')
        springs = parts[0]
        groups = [int(g) for g in parts[1].split(',')]
        rows.append((springs, groups))

def generate(s):
    result = []
    if '?' not in s:
        result.append(s)
    else:
        result.extend(generate(s.replace('?', '#', 1)))
        result.extend(generate(s.replace('?', '.', 1)))
    return result

def is_valid(springs, groups):
    spring_groups = [len(p) for p in re.split('[.]+', springs) if p != '']
    return spring_groups == groups

total = 0
for r in rows:
    total += len([s for s in generate(r[0]) if is_valid(s, r[1])])
print(total)

total = 0
for r in rows:
    row_total = 0
    unfolded_springs = ''
    unfolded_groups = []
    for _ in range(4):
        unfolded_springs += r[0] + '?'
        unfolded_groups.extend(r[1])
    unfolded_springs += r[0]
    unfolded_groups.extend(r[1])
    for s in generate(unfolded_springs):
       if is_valid(s, unfolded_groups):
           row_total += 1
    print(f'{unfolded_springs},{unfolded_groups}: {row_total}')
    total += row_total
print(total)
