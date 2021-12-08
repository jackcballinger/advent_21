from pathlib import Path

import numpy as np

with open(Path(__file__).parent.parent / 'input_data' / 'day_4.txt') as f:
    data = f.read()

def remove_number(called_number, boards_dict):
    return (
        {
            board_num: {
                'board': [np.delete(row, np.where(row == called_number)) for row in board_data['board']],
                'transposed_board': [np.delete(row, np.where(row == called_number)) for row in board_data['transposed_board']]
            } for board_num, board_data in boards_dict.items()
        }
    )

def run_check(boards_dict):
    winning_boards = []
    for board_num, board_data in boards_dict.items():
        any_rows = any([np.size(row)==0 for row in board_data['board']])
        any_cols = any([np.size(row)==0 for row in board_data['transposed_board']])
        if any_rows:
            winning_boards.append((board_num, 'board'))
        if any_cols:
            winning_boards.append((board_num, 'transposed_board'))
    return winning_boards

numbers, *boards = data.split('\n\n')

numbers = [int(x) for x in numbers.split(',')]
boards = [np.array([list(map(int, x.split())) for x in board.splitlines()]) for board in boards]
transposed_boards = [np.transpose(board) for board in boards]
boards_dict = {board_number: {'board': board, 'transposed_board': transposed_board} for board_number, (board, transposed_board) in enumerate(zip(boards, transposed_boards))}

# part 1
i = 0
while True:
    called_number = numbers[i]
    boards_dict = remove_number(called_number, boards_dict)
    board_check = run_check(boards_dict)
    if board_check:
        break
    i+=1

part_1 = sum(np.concatenate(boards_dict[board_check[0][0]][board_check[0][1]]).ravel().tolist()) * called_number
# 10374

numbers, *boards = data.split('\n\n')

numbers = [int(x) for x in numbers.split(',')]
boards = [np.array([list(map(int, x.split())) for x in board.splitlines()]) for board in boards]
transposed_boards = [np.transpose(board) for board in boards]
boards_dict = {board_number: {'board': board, 'transposed_board': transposed_board} for board_number, (board, transposed_board) in enumerate(zip(boards, transposed_boards))}


# part 2
cur_boards_dict = boards_dict.copy()
i = 0
while True:
    called_number = numbers[i]
    cur_boards_dict = remove_number(called_number, cur_boards_dict)
    board_check = run_check(cur_boards_dict)
    if board_check:
        for winning_board in list(set([x[0] for x in board_check])):
            cur_boards_dict.pop(winning_board)
    if len(cur_boards_dict) == 1:
        losing_board = cur_boards_dict
    if len(cur_boards_dict) == 0:
        losing_called_number = called_number
        break
    i+=1

part_2 = sum([num for num in [np.concatenate(v['board']).ravel() for v in losing_board.values()][0] if num != losing_called_number]) * losing_called_number
# 24742
