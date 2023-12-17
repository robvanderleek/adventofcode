#!/usr/bin/env python3
import re
from functools import cache

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
    g = list(groups)
    return spring_groups == g

@cache
def check(s, groups):
    if len(groups) == 0:
        if '#' not in s:
            return 1
        else:
            return 0
    s = s.strip('.')
    dot_index = s.find('.')
    question_index = s.find('?')
    if question_index >= 0 and (question_index < dot_index or dot_index < 0):
        return \
            check(s.replace('?', '#', 1), groups) + \
            check(s.replace('?', '.', 1), groups)
    else:
        if dot_index < 0 and len(s) == groups[0]:
            return check('', groups[1:])
        elif dot_index == groups[0]:
            return check(s[dot_index:], groups[1:])
        else:
            return 0

total = 0
for r in rows:
    springs = ''
    groups = []
    for i in range(5):
        springs += r[0]
        springs += '?' if i < 4 else ''
        groups.extend(r[1])
    valid = check(springs, tuple(groups))
    total += valid

print(total)
