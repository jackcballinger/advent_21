from pathlib import Path

with open(Path(__file__).parent.parent / 'input_data' / 'day_1.txt') as f:
    data = [int(x) for x in f.read().splitlines()]

# part 1
part_1 = sum([(data[i+1]-data[i])>0 for i in range(len(data)-1)])
# 1121

# part 2
part_2 = sum([(sum([data[i], data[i-1], data[i-2]])-sum([data[i-1], data[i-2], data[i-3]]))>0  for i in range(3, len(data))])
# 1065