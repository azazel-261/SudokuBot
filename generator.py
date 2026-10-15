import copy

from board import Board
import solver
import random

def generate_solved():
    board = Board()

    for sub in [0, 3, 6]:
        rand = list(range(1, 10))
        random.shuffle(rand)

        for i in range(9):
            sub_row = i // 3
            sub_col = i % 3

            board.data[sub + sub_row][sub + sub_col] = rand[i]

    return solver.get_random_solution(board)

def unsolve(_board: Board, remove_target: int):
    board = copy.deepcopy(_board)

    if remove_target > 80 or remove_target < 0:
        return board

    removed = 0
    available = list(range(81))

    while removed < remove_target and available:
        to_remove = random.choice(available)
        available.remove(to_remove)

        row = to_remove // 9
        col = to_remove % 9

        tmp = board.data[row][col]
        board.data[row][col] = 0

        if solver.count_valid_solutions(board) > 1:
            board.data[row][col] = tmp
            continue

        removed += 1

    return board





