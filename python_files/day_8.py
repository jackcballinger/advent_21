from collections import Counter
from itertools import chain
from pathlib import Path

with open(Path(__file__).parent.parent / 'input_data' / 'day_8.txt') as f:
    data = f.read().splitlines()

# globals
unique_segment_lengths = [2,4,3,7]
unique_segment_lengths_dict = {2:1,4:4,3:7,7:8}
segment_lengths_dict = {**unique_segment_lengths_dict,0:6,2:5,3:5,5:5,6:6,9:6}
unique_segment_appearences = {9:'f',4:'e',6:'b'}
segment_appearences = {**unique_segment_appearences,'a':8,'c':8,'d':7,'g':7}
number_dict = {'abcefg':0,'cf':1,'acdeg':2,'acdfg':3,'bcdf':4,'abdfg':5,'abdefg':6,'acf':7,'abcdefg':8,'abcdfg':9}

# format data functions
def format_part_1_data(input_data):
    return [[len(y) for y in x.split('|')[1].strip().split()] for x in input_data]

def format_part_2_data(input_data):
    return [[y.strip() for y in x.split('|')[0].split()] for x in input_data], [[y.strip() for y in x.split('|')[1].split()] for x in input_data]

# solving functions
def map_patterns(initial_pattern_dict, signal_pattern):
    output_mapping = {}
    output_mapping['a'] = list(set(initial_pattern_dict[7]) - set(initial_pattern_dict[1]))[0]
    letter_counts = Counter(list(chain.from_iterable(signal_pattern)))
    output_mapping = {**output_mapping, **{unique_segment_appearences[length]: letter for letter, length in letter_counts.items() if length in unique_segment_appearences}}
    one_characters = [x for x in [signal for signal in signal_pattern if len(signal)==2][0]]
    output_mapping['c'] = [x for x in one_characters if x not in output_mapping.values()][0]
    output_mapping['d'] = [x for x in initial_pattern_dict[4] if x not in output_mapping.values()][0]
    output_mapping['g'] = [x for x in list(set(chain.from_iterable(signal_pattern))) if x not in output_mapping.values()][0]
    return output_mapping

def decode_output_values(input_output_values, mappings):
    return int(''.join([str(number_dict[''.join(sorted([mappings[y] for y in x]))]) for x in input_output_values]))

# format data
part_1_data = format_part_1_data(data)
signal_patterns, output_values = format_part_2_data(data)

# part 1
part_1 = len([x for x in list(chain.from_iterable(part_1_data)) if x in unique_segment_lengths])
# 514

# part 2
initial_patterns = [{unique_segment_lengths_dict[len(pattern)]:pattern for pattern in signal_pattern if len(pattern) in unique_segment_lengths} for signal_pattern in signal_patterns]
pattern_mappings = [map_patterns(initial_pattern_dict, signal_pattern) for initial_pattern_dict, signal_pattern in zip(initial_patterns, signal_patterns)]
reverse_pattern_mappings = [{v:k for k, v in signal_pattern_mapping.items()} for signal_pattern_mapping in pattern_mappings]
decoded_output_values = [decode_output_values(output_value, reverse_pattern_mapping) for output_value, reverse_pattern_mapping in zip(output_values, reverse_pattern_mappings)]
part_2 = sum(decoded_output_values)
# 1012272
