#!/usr/bin/env python3

grid = []
with open('input.txt') as infile:
    lines = infile.readlines()
    for line in lines:
        grid.append([int(n) for n in line.strip()])

# right: 0, down: 1, left: 2, up: 3
def can_go(pos, direction, history, length):
    if history == direction and length + 1 > 2:
        return False
    if direction == 0 and history == 2:
        return False
    if direction == 1 and history == 3:
        return False
    if direction == 3 and history == 1:
        return False
    if direction == 2 and history == 0:
        return False
    if pos[0] < 0 or pos[0] >= len(grid) or pos[1] < 0 or \
            pos[1] >= len(grid[0]):
        return False
    return True
    
min_loss = {}

def dijkstra():
    heads = [(0, (0, 0), -1, 0)]
    while True:
        heads.sort(key=lambda h: (h[0], h[2], h[3]), reverse=True)
        head = heads.pop()
        key = (head[1], head[2], head[3])
        loss = head[0]
        if key in min_loss and min_loss[key] <= loss:
            continue
        if head[1] == (len(grid) - 1, len(grid[0]) - 1):
            return head
        min_loss[key] = loss 
        history = head[2]
        length = head[3]
        right = (head[1][0], head[1][1] + 1)
        if can_go(right, 0, history, length):
            new_loss = loss + grid[right[0]][right[1]]
            new_length = length + 1 if history == 0 else 0
            heads.append((new_loss, right, 0, new_length))
        down = (head[1][0] + 1, head[1][1])
        if can_go(down, 1, history, length):
            new_loss = loss + grid[down[0]][down[1]]
            new_length = length + 1 if history == 1 else 0
            heads.append((new_loss, down, 1, new_length))
        up = (head[1][0] - 1, head[1][1])
        if can_go(up, 3, history, length):
            new_loss = loss + grid[up[0]][up[1]]
            new_length = length + 1 if history == 3 else 0
            heads.append((new_loss, up, 3, new_length))
        left = (head[1][0], head[1][1] - 1)
        if can_go(left, 2, history, length):
            new_loss = loss + grid[left[0]][left[1]]
            new_length = length + 1 if history == 2 else 0
            heads.append((new_loss, left, 2, new_length))

print(dijkstra())
