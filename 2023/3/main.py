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

numbers = []
for y, row in enumerate(grid):
    for x, number in get_row_numbers(row):
        num_len = len(str(number))
        neighbours = [(x - 1, y), (x + num_len, y)] + \
            [(i, y - 1) for i in range(x - 1, x + num_len + 1)] + \
            [(i, y + 1) for i in range(x - 1, x + num_len + 1)]
        for coord in neighbours:
            if is_symbol(grid, coord[0], coord[1]):
                numbers.append(number)
            
print(sum(numbers))

def is_neighbour(num_x, num_y, num, x, y):
    num_len = len(str(num))
    neighbours = [(num_x - 1, num_y), (num_x + num_len, num_y)] + \
        [(i, num_y - 1) for i in range(num_x - 1, num_x + num_len + 1)] + \
        [(i, num_y + 1) for i in range(num_x - 1, num_x + num_len + 1)]
    return (x, y) in neighbours
    

ratios = []
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c != '*':
            continue
        numbers = []
        if y > 0:
            for num_x, num in get_row_numbers(grid[y - 1]):
                if is_neighbour(num_x, y - 1, num, x, y):
                    numbers.append(num)
        for num_x, num in get_row_numbers(row):
            if is_neighbour(num_x, y, num, x, y):
                numbers.append(num)
        if y < len(grid) - 1:
            for num_x, num in get_row_numbers(grid[y + 1]):
                if is_neighbour(num_x, y + 1, num, x, y):
                    numbers.append(num)
        if len(numbers) == 2:
            ratios.append(numbers[0] * numbers[1])
print(sum(ratios))         
