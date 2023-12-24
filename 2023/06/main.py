#!/usr/bin/env python3
import math
import re

with open('input-small.txt') as infile:
    lines = infile.readlines()

times = [t for t in re.split('\s+', lines[0].split(':')[1].strip())]
distances = [d for d in re.split('\s+', lines[1].split(':')[1].strip())]

ways = []
for index, t in enumerate([int (t) for t in times]):
    way = 0
    for i in range(1, t + 1):
        if i * (t - i) > int(distances[index]):
            way += 1
    ways.append(way)

print(math.prod(ways))

time = int(''.join(times))
distance = int(''.join(distances))

ways = 0
for i in range(1, time + 1):
    if i * (time - i) > distance:
        ways += 1
 
print(ways)
