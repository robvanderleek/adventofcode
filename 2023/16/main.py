#!/usr/bin/env python3

with open('input-small.txt') as infile:
    lines = infile.readlines()

grid = []
for line in lines:
    grid.append([c for c in line.strip()])

beams = [(0, 3, 'down')]
visited = []

def trace(beam):
    x = beam[1]
    y = beam[0]
    direction = beam[2]
    while True:
        if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
            return 
        tile = grid[y][x]
        if (y, x, direction) in visited:
            return
        else: 
            visited.append((y, x, direction))
        if tile == '|':
            if direction == 'left' or direction == 'right':
                beams.append((y - 1, x, 'up')) 
                beams.append((y + 1, x, 'down')) 
                return
        elif tile == '-':
            if direction == 'up' or direction == 'down':
                beams.append((y, x - 1, 'left')) 
                beams.append((y, x + 1, 'right')) 
                return
        elif tile == '\\':
            if direction == 'up':
                beams.append((y, x - 1, 'left')) 
                return
            elif direction == 'down':
                beams.append((y, x + 1, 'right')) 
                return
            if direction == 'right':
                beams.append((y + 1, x, 'down')) 
                return
            elif direction == 'left':
                beams.append((y - 1, x, 'up')) 
                return
        elif tile == '/':
            if direction == 'up':
                beams.append((y, x + 1, 'right')) 
                return
            elif direction == 'down':
                beams.append((y, x - 1, 'left')) 
                return
            if direction == 'right':
                beams.append((y - 1, x, 'up')) 
                return
            elif direction == 'left':
                beams.append((y + 1, x, 'down')) 
                return
        if direction == 'right':
            x += 1
        elif direction == 'left':
            x -= 1
        elif direction == 'up':
            y -= 1
        elif direction == 'down':
            y += 1

while beams:
    trace(beams.pop())

visited = set([(v[0], v[1]) for v in visited])
print(visited)

for y, row in enumerate(grid):
    line = ''
    for x, col in enumerate(row):
        if (y, x) in visited:
            line += '#' 
        else:
            line += '.'
    print(line)
print(len(visited))
