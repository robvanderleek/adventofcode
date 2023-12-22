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
        self._inputs = []

    def add_input(self, name):
        self._inputs.append(name)
        self._memory[name] = 'low'

    def process(self, name_from, pulse, stack):
        self._memory[name_from] = pulse
        if not 'low' in self._memory.values():
            for d in self._destinations:
                stack.append(self._name, d, 'low') 
        else:
            for d in self._destinations:
                stack.append(self._name, d, 'high') 

class FlipFlop:
    def __init__(self, name, destinations):
        self._name = name
        self._destinations = destinations
        self._memory = 'low' 
        self._inputs = []

    def add_input(self, name):
        self._inputs.append(name) 

    def process(self, name_from, pulse, stack):
        if pulse == 'low':
            self._memory = 'high' if self._memory == 'low' else 'low'
            for d in self._destinations:
                stack.append(self._name, d, self._memory)

class Output:

    def add_input(self, name):
        pass

    def process(self, name_from, pulse, stack):
        pass

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
    if operation == 'broadcaster':
        continue
    for operand in operands:
        if operand not in modules:
            modules[operand] = Output()
        modules[operand].add_input(operation[1:])
    

class Stack:
    def __init__(self):
        self._stack = [] 
        self._low_count = 0
        self._high_count = 0

    def append(self, name_from, name_to, pulse):
        if pulse == 'low':
            self._low_count += 1
        else:
            self._high_count += 1
        self._stack.append((name_from, name_to, pulse))

    def next(self):
        return self._stack.pop(0)

    def is_empty(self):
        return len(self._stack) == 0

stack = Stack()
for _ in range(1000):
    stack.append('button', 'broadcaster', 'low')
    while not stack.is_empty():
        [name_from, name_to, pulse] = stack.next()
        # print(f'{name_from} -{pulse}-> {name_to}')
        if name_to in modules:
            modules[name_to].process(name_from, pulse, stack)
    # print('===')

print(f'low = {stack._low_count}')
print(f'high = {stack._high_count}')
print(stack._low_count * stack._high_count)
