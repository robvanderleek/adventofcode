#!/usr/bin/env python3

with open('input.txt') as infile:
    lines = infile.readlines()
    rows = []
    for line in lines:
        rows.append([c for c in line.strip()])
    platform = tuple(tuple(r) for r in rows)

def tilt_north(p):
    pl = [list(r) for r in p]
    while True:
        changed = False
        for idx, row in enumerate(pl):
            if idx <= len(pl) - 2:
                next_row = pl[idx + 1]
                for idx_x in range(len(row)):
                    if row[idx_x] == '.' and next_row[idx_x] == 'O':
                        row[idx_x] = 'O'
                        next_row[idx_x] = '.'
                        changed = True
        if not changed:
            break
    return tuple(tuple(r) for r in pl)

def tilt_south(p):
    pl = [list(r) for r in p]
    while True:
        changed = False
        for idx_y in range(len(pl) - 1, 0, -1):
            row = pl[idx_y]
            prev_row = pl[idx_y - 1]
            for idx_x in range(len(row)):
                if row[idx_x] == '.' and prev_row[idx_x] == 'O':
                    row[idx_x] = 'O'
                    prev_row[idx_x] = '.'
                    changed = True
        if not changed:
            break
    return tuple(tuple(r) for r in pl)

def tilt_east(p):
    pl = [list(r) for r in p]
    while True:
        changed = False
        for idx_y, row in enumerate(pl):
            for idx_x in range(len(row) - 1, 0, -1):
                if row[idx_x] == '.' and row[idx_x - 1] == 'O':
                    row[idx_x] = 'O'
                    row[idx_x - 1] = '.'
                    changed = True
        if not changed:
            break
    return tuple(tuple(r) for r in pl)

def tilt_west(p):
    pl = [list(r) for r in p]
    while True:
        changed = False
        for idx_y, row in enumerate(pl):
            for idx_x in range(len(row) - 1):
                if row[idx_x] == '.' and row[idx_x + 1] == 'O':
                    row[idx_x] = 'O'
                    row[idx_x + 1] = '.'
                    changed = True
        if not changed:
            break
    return tuple(tuple(r) for r in pl)

def calc_load(p):
    load = 0
    for idx, row in enumerate(p):
        load += (len(p) - idx) * len([c for c in row if c == 'O'])
    return load 

def cycle(p):
    return tilt_east(tilt_south(tilt_west(tilt_north(p))))

full_cycles = []
index = -1
cycle_index = -1
for i in range(1000000000):
    platform = cycle(platform)
    if platform in full_cycles:
        cycle_index = full_cycles.index(platform)
        index = i
        break
    full_cycles.append(platform)
cycles_left = (1000000000 - index) % (index - cycle_index)
for i in range(cycles_left - 1):
    platform = cycle(platform)
print(calc_load(platform))
