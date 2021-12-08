from collections import Counter

from pathlib import Path

with open(Path(__file__).parent.parent / 'input_data' / 'day_3.txt') as f:
    data = f.read().splitlines()

# part 1
gamma = int(''.join([max(set([row[i] for row in data]), key=[row[i] for row in data].count) for i in range(len(data[0]))]), 2)
epsilon = int(''.join([min(set([row[i] for row in data]), key=[row[i] for row in data].count) for i in range(len(data[0]))]), 2)

part_1 = gamma*epsilon
# 741950

# part 2
oxygen_generator_rating_list = data.copy()
i = 0
while True:
    most_common_bit = Counter([row[i] for row in oxygen_generator_rating_list]).most_common()
    if len(set([x[1] for x in most_common_bit])) == 1:
        most_common_bit = '1'
    else:
        most_common_bit = most_common_bit[0][0]
    oxygen_generator_rating_list = [x for x in oxygen_generator_rating_list if x[i] == most_common_bit]
    if len(oxygen_generator_rating_list) == 1:
        break
    i += 1

co2_scrubber_rating_list = data.copy()
i = 0
while True:
    least_common_bit = Counter([row[i] for row in co2_scrubber_rating_list]).most_common()
    if len(set([x[1] for x in least_common_bit])) == 1:
        least_common_bit = '0'
    else:
        least_common_bit = least_common_bit[-1][0]
    co2_scrubber_rating_list = [x for x in co2_scrubber_rating_list if x[i] == least_common_bit]
    if len(co2_scrubber_rating_list) == 1:
        break
    i += 1

oxygen_generator_rating = int(oxygen_generator_rating_list[0],2)
co2_scrubber_rating = int(co2_scrubber_rating_list[0],2)
part_2 = oxygen_generator_rating * co2_scrubber_rating
# 903810