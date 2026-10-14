import copy
from dataclasses import dataclass
from board import Board

@dataclass
class BoardMoveTrace:
    index: int
    chosen_number_index: int

class RollbackError(Exception):
    pass

def rollback_to_last_decision(board: Board, stack: list[BoardMoveTrace]):
    while True:
        try:
            trace = stack[-1]
        except IndexError:
            print("Nowhere to roll back!")
            raise RollbackError

        i = trace.index
        col = i % 9
        row = (i - col) // 9
        board.data[row][col] = 0

        options = board.find_valid_numbers(row, col)
        if len(options) <= trace.chosen_number_index + 1:
            stack.pop()
        else:
            return i

def solve(_board: Board):
    board = copy.deepcopy(_board)
    stack: list[BoardMoveTrace] = []

    i = 0

    while i < 81:
        col = i % 9
        row = (i - col) // 9

        if board.data[row][col]:
            i += 1
            continue

        options = board.find_valid_numbers(row, col)
        if options:
            board.data[row][col] = options[0]
            stack.append(BoardMoveTrace(i, 0))
            i += 1
            continue
        else:
            print("No valid numbers found")
            try:
                i = rollback_to_last_decision(board, stack)
            except RollbackError:
                print("Out of solution space")
                return board
            stack[-1].chosen_number_index += 1
            board.data[row][col] = options[stack[-1].chosen_number_index]
        board.print()
    return board

def count_valid_solutions(_board: Board):
    board = copy.deepcopy(_board)
    stack: list[BoardMoveTrace] = []

    solutions = 0

    i = 0

    while True:
        if i > 80:
            try:
                print("Reached the end, rolling back")
                solutions += 1
                i = rollback_to_last_decision(board, stack)
                col = i % 9
                row = (i - col) // 9
                options = board.find_valid_numbers(row, col)
                stack[-1].chosen_number_index += 1
                board.data[row][col] = options[stack[-1].chosen_number_index]
            except RollbackError:
                return solutions

        col = i % 9
        row = (i - col) // 9

        if board.data[row][col]:
            i += 1
            continue

        options = board.find_valid_numbers(row, col)
        if options:
            board.data[row][col] = options[0]
            stack.append(BoardMoveTrace(i, 0))
            i += 1
            continue
        else:
            print("No valid numbers found")
            try:
                i = rollback_to_last_decision(board, stack)
            except RollbackError:
                print("Out of solution space")
                return solutions
            stack[-1].chosen_number_index += 1
            board.data[row][col] = options[stack[-1].chosen_number_index]
        board.print()
    return solutions
