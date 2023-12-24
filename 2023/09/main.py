#!/usr/bin/env python3

with open('input.txt') as infile:
    lines = infile.readlines()
 
histories = []
for line in lines:
    history = [int(n) for n in line.strip().split(' ')]
    histories.append(history)

def next_value(history):
    if len([n for n in history if n == 0]) == len(history):
        return 0
    else:
        next_history = []
        for idx, n in enumerate(history):
            if idx <= len(history) - 2:
                next_history.append(history[idx + 1] - n)
        return history[-1] + next_value(next_history)

def previous_value(history):
    if len([n for n in history if n == 0]) == len(history):
        return 0
    else:
        next_history = []
        for idx, n in enumerate(history):
            if idx <= len(history) - 2:
                next_history.append(history[idx + 1] - n)
        return history[0] - previous_value(next_history)

print(sum([next_value(h) for h in histories]))
print(sum([previous_value(h) for h in histories]))
