#!/usr/bin/env python3

class Broadcaster:
    def __init__(self, destinations):
        self._destinations = destinations

    def process(self, name_from, pulse, stack):
        for d in self._destinations:
            stack.append('broadcaster', d, pulse) 

class Conjunction:
    def __init__(self, name, destinations):
        self._name = name
        self._destinations = destinations
        self._memory = {}

    def add_input(self, name):
        self._memory[name] = 'low'

    def process(self, name_from, pulse, stack):
        self._memory[name_from] = pulse
        if not 'low' in self._memory.values():
            for d in self._destinations:
                stack.append(self._name, d, 'low') 
            return 'low'        
        else:
            for d in self._destinations:
                stack.append(self._name, d, 'high') 
            return 'high'

class FlipFlop:
    def __init__(self, name, destinations):
        self._name = name
        self._destinations = destinations
        self._memory = 'low' 

    def add_input(self, name):
        pass

    def process(self, name_from, pulse, stack):
        if pulse == 'low':
            self._memory = 'high' if self._memory == 'low' else 'low'
            for d in self._destinations:
                stack.append(self._name, d, self._memory)

with open('input.txt') as infile:
    lines = infile.readlines()
modules = {}
for line in lines:
    parts = line.strip().split(' -> ')
    operation = parts[0]
    operands = parts[1].split(', ')
    if operation == 'broadcaster':
        modules['broadcaster'] = Broadcaster(operands)
    elif operation.startswith('&'):
        modules[operation[1:]] = Conjunction(operation[1:], operands) 
    elif operation.startswith('%'):
        modules[operation[1:]] = FlipFlop(operation[1:], operands) 

for line in lines:
    parts = line.strip().split(' -> ')
    operation = parts[0]
    operands = parts[1].split(', ')
    if operation != 'broadcaster':
        for operand in operands:
            if operand in modules:
                modules[operand].add_input(operation[1:])

class Stack:
    def __init__(self):
        self._stack = [] 
        self.count = {'low': 0, 'high': 0}

    def append(self, name_from, name_to, pulse):
        self.count[pulse] += 1
        self._stack.append((name_from, name_to, pulse))

    def next(self):
        return self._stack.pop(0)

    def is_empty(self):
        return len(self._stack) == 0

stack = Stack()
iterations = {}
for i in range(10000):
    stack.append('button', 'broadcaster', 'low')
    while not stack.is_empty():
        [name_from, name_to, pulse] = stack.next()
        if name_to in modules:
            result = modules[name_to].process(name_from, pulse, stack)
            if name_to in ['nx', 'sp', 'cc', 'jq'] and \
                name_to not in iterations and result == 'high':
                iterations[name_to] = i + 1
    if 'nx' in iterations and 'sp' in iterations and 'cc' in iterations \
        and 'jq' in iterations:  
            break

print(stack.count['low'] * stack.count['high'])
print(iterations['nx'] * iterations['sp'] * iterations['cc'] * iterations['jq'])
