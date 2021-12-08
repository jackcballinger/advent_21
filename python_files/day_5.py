from collections import Counter
from itertools import chain
from pathlib import Path

import numpy as np

with open(Path(__file__).parent.parent / 'input_data' / 'day_5.txt') as f:
    data = f.read().splitlines()

def format_data(input_data):
    return [
        {
            'start': (int(x.split('->')[0].strip().split(',')[0]), int(x.split('->')[0].strip().split(',')[1])),
            'end': (int(x.split('->')[1].strip().split(',')[0]), int(x.split('->')[1].strip().split(',')[1]))
        } for x in input_data
    ]

def increase_x_coord(input_coordinates):
    diff = input_coordinates['end'][0] - input_coordinates['start'][0]
    if diff < 0:
        return [(input_coordinates['start'][0] + x,input_coordinates['start'][1]) for x in range(diff, 1)]
    return [(input_coordinates['start'][0] + x,input_coordinates['start'][1]) for x in range(0, diff+1)]

def increase_y_coord(input_coordinates):
    diff = input_coordinates['end'][1] - input_coordinates['start'][1]
    if diff < 0:
        return [(input_coordinates['start'][0],input_coordinates['start'][1] + x) for x in range(diff, 1)]
    return [(input_coordinates['start'][0],input_coordinates['start'][1] + x) for x in range(0, diff+1)]

def increase_x_and_y_coord(input_coordinates):
    x_diff = input_coordinates['end'][0] - input_coordinates['start'][0]    
    y_diff = input_coordinates['end'][1] - input_coordinates['start'][1]
    assert abs(x_diff) == abs(y_diff)
    x_coords = [input_coordinates['start'][0] + x for x in range(0, x_diff-1, -1)] if x_diff < 0 else [input_coordinates['start'][0] + x for x in range(0, x_diff+1)]
    y_coords = [input_coordinates['start'][1] + y for y in range(0, y_diff-1, -1)] if y_diff < 0 else [input_coordinates['start'][1] + y for y in range(0, y_diff+1)]

    return list(zip(x_coords, y_coords))

formatted_data = format_data(data)

part_1_coords, part_2_coords = [], []
for coordinate in formatted_data:
    if (coordinate['start'][0] != coordinate['end'][0]) and (coordinate['start'][1] != coordinate['end'][1]):
        part_2_coords.extend(increase_x_and_y_coord(coordinate))
    elif (coordinate['start'][0] != coordinate['end'][0]) and (coordinate['start'][1] == coordinate['end'][1]):  
        part_1_coords.extend(increase_x_coord(coordinate))
        part_2_coords.extend(increase_x_coord(coordinate))
    elif (coordinate['start'][1] != coordinate['end'][1]) and (coordinate['start'][0] == coordinate['end'][0]):        
        part_1_coords.extend(increase_y_coord(coordinate)) 
        part_2_coords.extend(increase_y_coord(coordinate))     

# part 1
part_1 = len([k for k,v in Counter(part_1_coords).items() if v>=2])
# 8060

# part 2
part_2 = len([k for k,v in Counter(part_2_coords).items() if v>=2])
# 21577
pass