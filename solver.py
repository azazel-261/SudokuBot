import copy, random, subprocess
from dataclasses import dataclass

from board import Board


@dataclass
class BoardMoveTrace:
    index: int
    options: list[int]
    option_index: int



class RollbackError(Exception):
    pass


def rollback_to_last_decision(board: Board, stack: list[BoardMoveTrace]):
    while True:
        try:
            trace = stack[-1]
        except IndexError:
            raise RollbackError

        i = trace.index
        col = i % 9
        row = i // 9
        board.data[row][col] = 0

        options = board.find_valid_numbers(row, col)
        if len(options) <= trace.option_index + 1:
            stack.pop()
        else:
            return i


def solve(_board: Board):
    board = copy.deepcopy(_board)
    stack: list[BoardMoveTrace] = []

    i = 0

    while i < 81:
        col = i % 9
        row = i // 9

        if board.data[row][col]:
            i += 1
            continue

        options = board.find_valid_numbers(row, col)
        if options:
            board.data[row][col] = options[0]
            stack.append(BoardMoveTrace(i, options, 0))
            i += 1
            continue
        else:
            try:
                i = rollback_to_last_decision(board, stack)
                col = i % 9
                row = i // 9
            except RollbackError:
                return None

            options = stack[-1].options
            stack[-1].option_index += 1
            board.data[row][col] = options[stack[-1].option_index]
    return board


def get_random_solution(_board: Board):
    board = copy.deepcopy(_board)
    stack: list[BoardMoveTrace] = []

    i = 0

    while i < 81:
        col = i % 9
        row = i // 9

        if board.data[row][col]:
            i += 1
            continue

        options = board.find_valid_numbers(row, col)
        if options:
            random.shuffle(options)
            board.data[row][col] = options[0]
            stack.append(BoardMoveTrace(i, options, 0))
            i += 1
            continue
        else:
            try:
                i = rollback_to_last_decision(board, stack)
                col = i % 9
                row = i // 9
            except RollbackError:
                return board

            options = stack[-1].options
            stack[-1].option_index += 1
            board.data[row][col] = options[stack[-1].option_index]
    return board


def count_valid_solutions(_board: Board):
    board = copy.deepcopy(_board)
    stack: list[BoardMoveTrace] = []

    solutions = 0

    i = 0

    while True:
        if i > 80:
            try:
                solutions += 1
                i = rollback_to_last_decision(board, stack)
                col = i % 9
                row = i // 9
                options = board.find_valid_numbers(row, col)
                stack[-1].option_index += 1
                board.data[row][col] = options[stack[-1].option_index]
            except RollbackError:
                return solutions

        col = i % 9
        row = i // 9

        if board.data[row][col]:
            i += 1
            continue

        options = board.find_valid_numbers(row, col)
        if options:
            board.data[row][col] = options[0]
            stack.append(BoardMoveTrace(i, options, 0))
            i += 1
            continue
        else:
            try:
                i = rollback_to_last_decision(board, stack)
                col = i % 9
                row = i // 9
            except RollbackError:
                return solutions

            options = stack[-1].options
            stack[-1].option_index += 1
            board.data[row][col] = options[stack[-1].option_index]
    return solutions


# Time-consuming as hell so I gave up, maybe I'll come back here later
def get_all_solutions(_board: Board):
    board = copy.deepcopy(_board)
    stack: list[BoardMoveTrace] = []

    i = 0

    while True:
        if i > 80:
            try:
                yield copy.deepcopy(board)
                i = rollback_to_last_decision(board, stack)
                col = i % 9
                row = i // 9
                options = board.find_valid_numbers(row, col)
                stack[-1].option_index += 1
                board.data[row][col] = options[stack[-1].option_index]
            except RollbackError:
                break

        col = i % 9
        row = i // 9

        if board.data[row][col]:
            i += 1
            continue

        options = board.find_valid_numbers(row, col)
        if options:
            board.data[row][col] = options[0]
            stack.append(BoardMoveTrace(i, options, 0))
            i += 1
            continue
        else:
            try:
                i = rollback_to_last_decision(board, stack)
                col = i % 9
                row = i // 9
            except RollbackError:
                break

            options = stack[-1].options
            stack[-1].option_index += 1
            board.data[row][col] = options[stack[-1].option_index]
