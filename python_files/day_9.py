from pathlib import Path

import numpy as np

with open(Path(__file__).parent.parent / 'input_data' / 'day_9.txt') as f:
    data = f.read().splitlines()

def format_data(input_data):
    return np.array([[list([int(z) for z in y]) for y in x.split()][0] for x in input_data])

directions_dict = {
    'up': [-1,0],
    'down': [1,0],
    'left': [0,-1],
    'right': [0,1]
}

formatted_data = format_data(data)

pass