#!/usr/bin/env python3
import re
import functools

rows = []

with open('input.txt') as infile:
    lines = infile.readlines()
    for line in lines:
        parts = line.strip().split(' ')
        springs = parts[0]
        groups = [int(g) for g in parts[1].split(',')]
        rows.append((springs, groups))

@functools.lru_cache(maxsize=None)
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

def check(s, groups):
    result = 0
    if '?' not in s:
        if is_valid(s, groups):
            result += 1
    else:
        result += check(s.replace('?', '#', 1), groups)
        result += check(s.replace('?', '.', 1), groups)
    return result

total = 0
for r in rows:
    total += check(r[0], r[1])

total = 0
for r in rows:
    row_total = 0
    springs = r[0]
    groups = []
    groups.extend(r[1])
    valid = [s for s in generate(springs) if is_valid(s, groups)]
    row_total += len(valid)
    for _ in range(4):
        groups.extend(r[1])
        next_valid = []
        for v in valid:
            next_valid.extend([s for s in generate(v + '.' + springs) if is_valid(s, groups)])
            next_valid.extend([s for s in generate(v + '#' + springs) if is_valid(s, groups)])
        valid = next_valid
        row_total = len(next_valid)
    print(row_total)
    total += row_total

        #unfolded_springs += r[0] + '?'
        #unfolded_groups.extend(r[1])
    #unfolded_springs += r[0]
    #unfolded_groups.extend(r[1])
    #row_total += check(unfolded_springs, unfolded_groups)
    #print(f'{unfolded_springs},{unfolded_groups}: {row_total}')
    #total += row_total
print(total)
