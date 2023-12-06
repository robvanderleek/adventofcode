#!/usr/bin/env python3
import sys

with open('input.txt') as infile:
    lines = infile.readlines()

seeds = [int(s) for s in lines[0].strip().split(': ')[1].split(' ')]
line_nr = 3

def parse_mapping(lines, line_nr):
    result = []
    while lines[line_nr].strip():
        mapping = lines[line_nr].strip().split(' ')
        result.append((int(mapping[0]), int(mapping[1]), int(mapping[2])))
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
            if number >= m[1] and number < (m[1] + m[2]):
                number = m[0] + (number - m[1])
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

for s in seeds:
    location = do_mappings(s, [seed_to_soil, soil_to_fertilizer, 
        fertilizer_to_water, water_to_light, light_to_temperature,
        temperature_to_humidity, humidity_to_location])

    if not lowest_location or location < lowest_location:
        lowest_location = location

print(lowest_location)
