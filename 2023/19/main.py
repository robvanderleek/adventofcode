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
            name = val[0]
            logic = val[1]
            workflows[name] = logic
        else:
            part = {}
            for c in line.strip()[1:-1].split(','):
                val = c.split('=') 
                part[val[0]] = int(val[1])
            parts.append(part)

def execute(workflow, part):
    rules = workflow.split(',')
    for rule in rules[:-1]:
        split = rule.split(':')
        exp = split[0]
        target = split[1]
        ch = exp[0]
        operator = exp[1]
        val = int(exp[2:])
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
