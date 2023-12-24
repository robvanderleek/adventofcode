#!/usr/bin/env python3  
from collections import Counter
from functools import cmp_to_key

with open('input.txt') as infile:
    lines = infile.readlines()
hands = []
for line in lines:
    parts = line.strip().split(' ')
    hands.append((parts[0], int(parts[1])))

def replace_jokers(cards):
    jokers = [c for c in cards if c == 'J']
    if len(jokers) == 0:
        return [cards]
    elif len(jokers) == 5:
        return ['AAAAA']
    else:
        order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        result = []
        for c in order:
            result.extend(replace_jokers(cards.replace('J', c, 1)))
        return result

def use_jokers(cards):
    combinations = replace_jokers(cards)
    return sort_cards_list([(c, c) for c in combinations])[-1]

def rank_cards(cards):
    counter = Counter(cards)
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

def compare_cards(cards1, cards2):
     order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', \
         'J']
     result = rank_cards(cards1[1]) - rank_cards(cards2[1])
     if result == 0:
         for idx, card in enumerate(cards1[0]):
             if order.index(card) < order.index(cards2[0][idx]):
                 return 1
             if order.index(card) > order.index(cards2[0][idx]):
                 return -1
     return result

def sort_cards_list(cards_list):
    return sorted(cards_list, key=cmp_to_key(compare_cards)) 

def sort_hands(hands):
    def compare(hand1, hand2):
        return compare_cards((hand1[0], hand1[2]), (hand2[0], hand2[2]))
        
    return sorted(hands, key=cmp_to_key(compare))

hands_with_strongest = []
for hand in hands:
    strongest = use_jokers(hand[0])[0]
    hand_with_strongest = (hand[0], hand[1], strongest)
    hands_with_strongest.append(hand_with_strongest)
hands_with_strongest = sort_hands(hands_with_strongest)
sum = 0
for index, hand in enumerate(hands_with_strongest):
    sum += (index + 1) * hand[1]
print(sum)
