#!/usr/bin/env python3

with open('input.txt') as infile:
    lines = infile.readlines()

directions = [d for d in lines[0].strip()]
dir_idx = 0

graph = {}

for line in lines[2:]:
    parts = line.strip().split(' = ')
    targets = parts[1][1:-1].split(', ')
    graph[parts[0]] = {'L': targets[0], 'R': targets[1]}

steps = 0
node = 'AAA'
while node != 'ZZZ':
    steps += 1
    node = graph[node][directions[dir_idx]]
    if dir_idx < len(directions) - 1:
        dir_idx += 1
    else:
        dir_idx = 0

print(steps)
