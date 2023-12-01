#!/usr/bin/env python3

substitutions = [('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), 
    ('five', '5'), ('six', '6'), ('seven', '7'), ('eight', '8'), ('nine', '9')]

def first_digit(s):
    index = 0
    while index < len(s):
        if s[index].isdigit():
            return s[index]
        for sub in substitutions:
            if s[index:].startswith(sub[0]):
                return sub[1]
        index += 1

def last_digit(s):
    index = len(s) - 1
    while index >= 0:
        if s[index].isdigit():
            return s[index]
        for sub in substitutions:
            if s[index:].startswith(sub[0]):
                return sub[1]
        index -= 1

with open('input2.txt') as infile:
    lines = [line.strip() for line in infile.readlines()]
numbers = []
for line in lines:
    number = int(f'{first_digit(line)}{last_digit(line)}')
    numbers.append(number)
print(sum(numbers))
