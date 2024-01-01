#!/usr/bin/env python3

maze = []
with open('input.txt') as infile:
    lines = infile.readlines()
    for line in lines:
        maze.append([c for c in line.strip()])

start = (0, 1)
end = (len(maze) - 1, len(maze[0]) - 2)
longest = []

def in_maze(pos):
    return pos[0] >= 0 and pos[0] < len(maze) and \
        pos[1] >= 0 and pos[1] < len(maze[0])
        
def valid_new_pos(pos, visited):
    return pos not in visited and in_maze(pos) and maze[pos[0]][pos[1]] != '#'

def get_neighbours(pos, visited):
    result = []
    new_pos = (pos[0] + 1, pos[1])
    if valid_new_pos(new_pos, visited):
        result.append(new_pos)
    new_pos = (pos[0] - 1, pos[1])
    if valid_new_pos(new_pos, visited):
        result.append(new_pos)
    new_pos = (pos[0], pos[1] + 1)
    if valid_new_pos(new_pos, visited):
        result.append(new_pos)
    new_pos = (pos[0], pos[1] - 1)
    if valid_new_pos(new_pos, visited):
        result.append(new_pos)
    return result 

def build_graph(maze):
    visited_nodes = set()
    heads = [start] 
    edges = set() 
    while heads:
        head = heads.pop(0)
        visited_nodes.add(head)
        for p in get_neighbours(head, set()):
            visited = [head]
            new_head = p
            nbs = get_neighbours(new_head, visited)
            while len(nbs) == 1:
                visited.append(new_head)
                new_head = nbs[0]
                nbs = get_neighbours(new_head, visited)
            if len(nbs) > 1:
                if not new_head in visited_nodes:
                    edges.add((head, new_head, len(visited))) 
                    heads.append(new_head)
            if new_head == end:
                edges.add((head, new_head, len(visited)))
    return edges    

def move(head):
    global longest
    pos = head[0]
    path = head[1]
    if pos == end and len(path) > len(longest):
        longest = path 
    else:
        result = []
        new_pos = (pos[0] + 1, pos[1])
        if valid_new_pos(new_pos, head):
            result.append(((pos[0] + 1, pos[1]), path + [pos]))
        new_pos = (pos[0] - 1, pos[1])
        if valid_new_pos(new_pos, head):
            result.append(((pos[0] - 1, pos[1]), path + [pos]))
        new_pos = (pos[0], pos[1] + 1)
        if valid_new_pos(new_pos, head):
            result.append(((pos[0], pos[1] + 1), path + [pos]))
        new_pos = (pos[0], pos[1] - 1)
        if valid_new_pos(new_pos, head):
            result.append(((pos[0], pos[1] - 1), path + [pos]))
        return result

def explore(edges):
    longest = 0
    heads = [(start, 0, {start})]
    while heads:
        pos, l, visited = heads.pop()
        if pos == end:
            if l > longest:
                longest = l
        else:
            outgoing = [e for e in edges if e[0] == pos or e[1] == pos]
            for out in outgoing:
                if out[0] == pos and not out[1] in visited:
                    heads.append((out[1], l + out[2], visited | {out[1]}))
                if out[1] == pos and not out[0] in visited:
                    heads.append((out[0], l + out[2], visited | {out[0]}))
    return longest

print(explore(build_graph(maze)))
