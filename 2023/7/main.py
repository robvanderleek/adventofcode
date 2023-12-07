#!/usr/bin/env python3  
from collections import Counter
from functools import cmp_to_key

with open('input.txt') as infile:
    lines = infile.readlines()

hands = []
for line in lines:
    parts = line.strip().split(' ')
    hands.append((parts[0], int(parts[1])))

def rank_hand(hand):
    counter = Counter(hand)
    counts = [i[1] for i in counter.most_common()]
    if counts[0] == 5:
        return 7
    elif counts[0] == 4:
        return 6
    elif counts[0] == 3 and counts[1] == 2:
        return 5
    elif counts[0] == 3:
        return 4
    elif counts[0] == 2 and counts[1] == 2:
        return 3
    elif counts[0] == 2:
        return 2
    else:
        return 1

def compare(hand1, hand2):
    order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    result = rank_hand(hand1[0]) - rank_hand(hand2[0])
    if result == 0:
        for index, card in enumerate(hand1[0]):
            if order.index(card) < order.index(hand2[0][index]):
                return 1
            if order.index(card) > order.index(hand2[0][index]):
                return -1
    return result
        
hands = sorted(hands, key=cmp_to_key(compare))
sum = 0
for index, hand in enumerate(hands):
    sum += (index + 1) * hand[1]
print(sum)
