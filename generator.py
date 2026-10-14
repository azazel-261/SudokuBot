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


