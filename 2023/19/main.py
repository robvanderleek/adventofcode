#!/usr/bin/env python3
import json

with open('input.txt') as infile:
    lines = infile.readlines()
    workflows = {} 
    parts = []
    in_workflows = True
    for line in lines:
        if line.strip() == '':
            in_workflows = False
            continue
        if in_workflows:
            workflow = []
            val = line.strip()[:-1].split('{')
            workflows[val[0]] = val[1]
        else:
            part = {}
            for c in line.strip()[1:-1].split(','):
                val = c.split('=') 
                part[val[0]] = int(val[1])
            parts.append(part)

def parse_exp(exp):
    ch = exp[0]
    operator = exp[1]
    val = int(exp[2:])
    return [ch, operator, val]

def revert(ch, operator, val):
    return [ch, '>', val - 1] if operator == '<' else [ch, '<', val + 1]

def execute(workflow, part):
    rules = workflow.split(',')
    for rule in rules[:-1]:
        split = rule.split(':')
        exp = split[0]
        target = split[1]
        [ch, operator, val] = parse_exp(exp)
        if operator == '<':
            if part[ch] < val:
                return target 
        else:
            if part[ch] > val:
                return target 
    return rules[-1]

def process(part):
    workflow = workflows['in']
    while True:
        result = execute(workflow, part)
        if result in ['A', 'R']:
            return result
        else: 
            workflow = workflows[result] 

result = 0
for p in parts:
    if process(p) == 'A':
        result += p['x'] + p['m'] + p['a'] + p['s']
print(result)

nodes = edges = []
for k, v in workflows.items():
    if not k in nodes:
        nodes.append(k)
    rules = v.split(',')
    exps = []
    for rule in rules[:-1]: 
        split = rule.split(':')
        exp = split[0]
        target = split[1]
        [ch, op, val] = parse_exp(exp)
        edges.append((k, target, exps + [[ch, op, val]]))
        exps.append(revert(ch, op, val))
    edges.append((k, rules[-1], exps))

def walk(node, end, path, paths, nodes):
    if node == end:
        paths.append(path)
        return paths
    else:
        for e in edges:
            if e[0] == node:
                walk(e[1], end, path + e[2], paths, nodes + [node])
    return paths

total = 0
for p in walk('in', 'A', [], [], []):
    b = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}
    for pb in p:
        ch_bounds = b[pb[0]]
        if pb[1] == '<' and ch_bounds[1] > pb[2] - 1:
            ch_bounds[1] = pb[2] - 1
        elif ch_bounds[0] < pb[2] + 1:
            ch_bounds[0] = pb[2] + 1
    total += (b['x'][1] - b['x'][0] + 1) * (b['m'][1] - b['m'][0] + 1) * \
             (b['a'][1] - b['a'][0] + 1) * (b['s'][1] - b['s'][0] + 1)
print(total)
