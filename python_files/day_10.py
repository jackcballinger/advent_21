from collections import deque, Counter
from pathlib import Path

with open(Path(__file__).parent.parent / 'input_data' / 'day_10.txt') as f:
    data = f.read().splitlines()

test_data = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".splitlines()

symbol_mapping = {
    '}':'{',
    ']':'[',
    ')':'(',
    '>':'<'
}
reversed_symbol_mapping = {v:k for k,v in symbol_mapping.items()}

part_1_symbol_scoring = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

part_2_symbol_scoring = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def find_corruption(line):
    current_characters = deque()
    for char in line:
        if len(current_characters) == 0:
            current_characters.append(char)
        if char in ['{','[','<','(']:
            current_characters.append(char)
        elif char in ['}',']','>',')'] and current_characters[-1] == symbol_mapping[char]:
            current_characters.pop()
        else:
            return char
    return False, list(reversed([reversed_symbol_mapping[x] for x in current_characters]))[:-1]

def get_total_score(input_missing_strings):
    tot = 0
    for item in input_missing_strings:
        tot = (tot*5)+part_2_symbol_scoring[item]
    return tot

# part 1
corrupt_lines = [(i, find_corruption(line)) for i, line in enumerate(data) if find_corruption(line)[0]]
part_1 = sum([part_1_symbol_scoring[k]*v for k, v in Counter([x[1] for x in corrupt_lines]).items()])
# 265527

# part 2
part_2_data = [line for i, line in enumerate(data) if i not in [x[0] for x in corrupt_lines]]
missing_strings = [find_corruption(line)[1] for line in part_2_data]
string_scores = [get_total_score(missing_string) for missing_string in missing_strings]
part_2 = list(sorted(string_scores))[int((len(string_scores))/2)]
# 3969823589
