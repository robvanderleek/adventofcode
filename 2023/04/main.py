#!/usr/bin/env python3
import re

with open('input.txt') as infile:
    lines = infile.readlines()

total = 0
multiplier = [1 for line in lines]

for index, line in enumerate(lines):
    [card, numbers] = line.strip().split(':')
    [winning, mine] = numbers.split('|')
    winning_numbers = [int(n) for n in re.split('\s+', winning.strip())]
    my_numbers = [int(n) for n in re.split('\s+', mine.strip())]
    card_winning = 0
    for n in my_numbers:
        if n in winning_numbers:
            card_winning += 1
    if card_winning > 0:
        total += pow(2, card_winning - 1)
        for i in range(1, card_winning + 1):
            if index + i >= len(lines):
                break 
            for j in range(multiplier[index]):
                multiplier[index + i] = multiplier[index + i] + 1

print(total)
print(sum(multiplier))
