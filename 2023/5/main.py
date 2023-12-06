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

[line_nr, seed_to_soil] = parse_mapping(lines, line_nr)
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
