#!/usr/bin/env python3
import random

def parse():
    nodes = set()
    edges = []
    with open('input.txt') as infile:
        lines = infile.readlines()
        for line in lines:
            parts = line.strip().split(': ')
            from_node = parts[0]
            nodes.add(from_node)
            to_nodes = parts[1].split(' ')
            for to_node in to_nodes:
                nodes.add(to_node)
                edges.append((from_node, to_node))
    return [nodes, edges]

while True:
    nodemap = {}
    [nodes, edges] = parse()
    while len(nodes) > 2:
        e = random.choice(edges)
        from_node = e[0]
        to_node = e[1]
        updated_edges = []
        for edge in edges:
            if edge[0] == from_node and edge[1] == to_node or \
               edge[1] == from_node and edge[0] == to_node:
                continue
            elif edge[0] == to_node:
                updated_edges.append((from_node, edge[1]))
            elif edge[1] == to_node:
                updated_edges.append((edge[0], from_node))
            else:
                updated_edges.append(edge)
        edges = updated_edges
        nodes.remove(to_node) 
        nodemap[from_node] = nodemap.get(from_node, 1) + nodemap.get(to_node, 1)
        nodemap.pop(to_node, None)
    
    if len(edges) == 3 and len(nodemap) == 2:
        items = list(nodemap.items())
        print(items[0][1] * items[1][1])
        break
