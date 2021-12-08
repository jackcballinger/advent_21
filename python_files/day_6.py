from pathlib import Path

import numpy as np

with open(Path(__file__).parent.parent / 'input_data' / 'day_6.txt') as f:
    data = f.read()

test_data = """3,4,3,1,2"""

def format_data(input_data):
    return np.array([int(x) for x in input_data.split(',')])

formatted_data = format_data(data)


# part 1
part_1_data = formatted_data.copy()
day = 1
n_days = 80
while day <= n_days:
    print(day)
    part_1_data -= 1
    part_1_data = np.append(part_1_data, np.count_nonzero(part_1_data == -1)*[8])
    part_1_data = np.where(part_1_data == -1, 6, part_1_data)
    day += 1
part_1 = len(part_1_data)
# 362639

# part 2
part_2_data = formatted_data.copy()
n_days = 256
fish = [0]*9
for num in part_2_data:
    fish[num] += 1
for _ in range(n_days):
    num_zero = fish[0]
    # shift fish down
    fish[:-1] = fish[1:]
    fish[8] = num_zero
    fish[6] += num_zero
part_2 = sum(fish)
# 1639854996917