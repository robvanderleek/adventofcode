#!/usr/bin/env python3
import math

with open('input.txt') as infile:
    lines = infile.readlines()
directions = [d for d in lines[0].strip()]

graph = {}
for line in lines[2:]:
    parts = line.strip().split(' = ')
    targets = parts[1][1:-1].split(', ')
    graph[parts[0]] = {'L': targets[0], 'R': targets[1]}

dir_idx = 0
steps = 0
nodes = [n for n in graph.keys() if n.endswith('A')]
finished = []
while len([n for n in nodes if not n.endswith('Z')]) > 0:
    steps += 1
    for idx, n in enumerate(nodes):
        if idx in [f[0] for f in finished]:
            continue
        nodes[idx] = graph[n][directions[dir_idx]]
        if nodes[idx].endswith('Z'):
            finished.append((idx, steps))
    if dir_idx < len(directions) - 1:
        dir_idx += 1
    else:
        dir_idx = 0
for f in finished:
    print(f'Finished node {f[0]} in {f[1]} steps')

highest = max([f[1] for f in finished])
total = highest
print(math.prod([f[1] for f in finished]))
while True:
    all_divisors = True
    for f in finished:
        if total % f[1] != 0:
            all_divisors = False
    if all_divisors:
        break
    else:
        total += highest
print(total)
