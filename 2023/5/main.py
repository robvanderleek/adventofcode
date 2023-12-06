#!/usr/bin/env python3
import sys

with open('input-small.txt') as infile:
    lines = infile.readlines()

seeds = [int(s) for s in lines[0].strip().split(': ')[1].split(' ')]
line_nr = 3

def parse_mapping(lines, line_nr):
    result = []
    while lines[line_nr].strip():
        mapping = lines[line_nr].strip().split(' ')
        start = int(mapping[1])
        end = start + int(mapping[2])
        shift = int(mapping[0]) - start
        result.append((start, end, shift))
        if line_nr < len(lines) - 1:
            line_nr += 1
        else:
            break
    if line_nr < len(lines) - 1:
        line_nr += 2
    return line_nr, result

def do_mappings(number, mappings):
    for mapping in mappings:
        for m in mapping:
            if number >= m[0] and number < m[1]:
                number += m[2]
                break
    return number

def do_range_mappings(ranges, mappings):
    result = []
    for mapping in mappings:
        updated_ranges = []
        for r in ranges:
            updated_range = []
            for m in mapping:
                # no overlap
                if m[1] < r[0] or m[0] > r[0] + (r[1] - 1):
                    continue
                # complete overlap
                if m[0] <= r[0] and m[1] >= r[0] + (r[1] - 1):
                    updated_range.append((r[0] + m[2], r[1]))
                else:
                    # left/middle/right overlap
                    left_len = (m[0] - r[0])
                    if left_len > 0:
                        updated_range.append((r[0], left_len))
                    middle_start = r[0] + max(left_len, 0)
                    middle_len = min(r[0] + r[1], m[1]) - middle_start
                    updated_range.append((middle_start + m[2], middle_len))
                    right_len = (r[0] + r[1]) - m[1]
                    if right_len > 0:
                        updated_range.append((r[0], right_len))
            if updated_range:
                updated_ranges.extend(updated_range)
            else:
                updated_ranges.extend(r)
        result = updated_ranges
    return result

[line_nr, seed_to_soil] = parse_mapping(lines, line_nr)

print(do_range_mappings([(79, 14), (45, 11)], [seed_to_soil]))

[line_nr, soil_to_fertilizer] = parse_mapping(lines, line_nr)
[line_nr, fertilizer_to_water] = parse_mapping(lines, line_nr)
[line_nr, water_to_light] = parse_mapping(lines, line_nr)
[line_nr, light_to_temperature] = parse_mapping(lines, line_nr)
[line_nr, temperature_to_humidity] = parse_mapping(lines, line_nr)
[line_nr, humidity_to_location] = parse_mapping(lines, line_nr)

lowest_location = None

while seeds:
    start = int(seeds.pop(0))
    end = start + int(seeds.pop(0))
    for s in range(start, end):
        location = do_mappings(s, [seed_to_soil, soil_to_fertilizer, 
            fertilizer_to_water, water_to_light, light_to_temperature,
            temperature_to_humidity, humidity_to_location])

        if not lowest_location or location < lowest_location:
            lowest_location = location
            print(f'New lowest: {lowest_location}')

print(lowest_location)
