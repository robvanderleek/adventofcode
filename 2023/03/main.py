#!/usr/bin/env python3

with open('input.txt') as infile:
    lines = [line.strip() for line in infile.readlines()]

grid = []
for line in lines:
    grid.append([c for c in line])

def get_row_numbers(row):
    result = []
    cur_index = 0
    cur_number = None
    for i, c in enumerate(row): 
        if c.isdigit():
            if cur_number is None:
                cur_index = i
                cur_number = str(c)
            else:
                cur_number += str(c)
        else:
            if cur_number:
                result.append((cur_index, int(cur_number)))
                cur_number = None
    if cur_number: 
        result.append((cur_index, int(cur_number)))
    return result

def is_symbol(grid, x, y):
    if y < 0 or y > len(grid) - 1:
        return False 
    if x < 0 or x > len(grid[y]) - 1:
        return False
    return grid[y][x] != '.' and not grid[y][x].isdigit()

def get_neighbours(x, y, number):
    num_len = len(str(number))
    return [(x - 1, y), (x + num_len, y)] + \
        [(i, y - 1) for i in range(x - 1, x + num_len + 1)] + \
        [(i, y + 1) for i in range(x - 1, x + num_len + 1)]

def are_neighbours(number_x, number_y, number, x, y):
    return (x, y) in get_neighbours(number_x, number_y, number)

numbers = []
for y, row in enumerate(grid):
    for x, number in get_row_numbers(row):
        for n in get_neighbours(x, y, number):
            if is_symbol(grid, n[0], n[1]):
                numbers.append(number)
print(sum(numbers))

ratios = []
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == '*':
            numbers = []
            if y > 0:
                numbers.extend([n for n_x, n in get_row_numbers(grid[y - 1])
                    if are_neighbours(n_x, y - 1, n, x, y)])
            numbers.extend([n for n_x, n in get_row_numbers(row) 
                if are_neighbours(n_x, y, n, x, y)])
            if y < len(grid) - 1:
                numbers.extend([n for n_x, n in get_row_numbers(grid[y + 1])
                    if are_neighbours(n_x, y + 1, n, x, y)])
            if len(numbers) == 2:
                ratios.append(numbers[0] * numbers[1])
print(sum(ratios))         
