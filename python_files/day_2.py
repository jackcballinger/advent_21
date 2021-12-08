from pathlib import Path

import numpy as np

with open(Path(__file__).parent.parent / 'input_data' / 'day_2.txt') as f:
    data = f.read().splitlines()

test_data = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

formatted_test_data = [(x.split(' ')[0], int(x.split(' ')[1])) for x in test_data.splitlines()]

movement_dict = {
    'forward': np.array([0, 1]),
    'up': np.array([-1, 0]),
    'down': np.array([1, 0])
}

updated_movement_dict = {
    'forward': np.array([0, 1])
}

aim_dict = {
    'up': -1,
    'down': 1
}

formatted_data = [(x.split(' ')[0], int(x.split(' ')[1])) for x in data]

# part 1
cur_position = np.array([0,0])
for move in formatted_data:
    cur_position += movement_dict[move[0]]*move[1]
part_1 = np.prod(cur_position)
# 1840243

# part 2
cur_position = np.array([0,0])
aim = 0
for move in formatted_data:
    cur_position += (updated_movement_dict.get(move[0],0)*move[1]) + ((aim * move[1])*np.array([1,0]) if move[0] == 'forward' else np.array([0,0]))
    aim += (aim_dict.get(move[0], 0))*move[1]
part_2 = np.prod(cur_position)
# 1727785422
