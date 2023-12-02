#!/usr/bin/env python3

with open('input.txt') as infile:
    lines = infile.readlines()

valid_games = []
game_powers = []

def is_valid_draw(marbles):
    for marble in marbles:
        [count, color] = marble.split(' ')
        if (color == 'red' and int(count) > 12) or \
           (color == 'green' and int(count) > 13) or \
           (color == 'blue' and int(count) > 14):
            return False
    return True 

def is_valid_game(games):
    for game in games:
        marbles = game.split(', ') 
        if not is_valid_draw(marbles):
            return False
    return True

def game_power(game_marbles):
    red = 0
    green = 0
    blue = 0 
    for marbles in game_marbles:
        for marble in marbles:
            [count, color] = marble.split(' ')
            if (color == 'red' and int(count) > red):
                red = int(count)
            if (color == 'green' and int(count) > green):
                green = int(count)
            if (color == 'blue' and int(count) > blue):
                blue = int(count)
    return red * green * blue

for line in lines:
    [game_id, all_games] = line.strip().split(': ')
    game_number = int(game_id.split(' ')[1])
    games = all_games.split('; ')
    if is_valid_game(games):
        valid_games.append(game_number)
    game_marbles = [game.split(', ') for game in games]
    game_powers.append(game_power(game_marbles))

print(sum(valid_games))
print(sum(game_powers))
