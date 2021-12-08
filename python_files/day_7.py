from pathlib import Path

with open(Path(__file__).parent.parent / 'input_data' / 'day_7.txt') as f:
    data = f.read()

test_data = """16,1,2,0,4,2,7,1,2,14"""

def format_data(input_data):
    return sorted([int(x) for x in input_data.split(',')])

formatted_data = format_data(data)

# part 1
median = formatted_data[len(formatted_data)//2]
part_1 = sum(abs(x-median) for x in formatted_data)
# 356922

# part 2
mean = sum(formatted_data)//len(formatted_data)
part_2 = sum(sum(range(1,abs(num-mean)+1)) for num in formatted_data)
# 100347031
pass