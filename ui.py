import pynput, subprocess
from colorama import Fore, Back

from board import Board

class ActionSelector:
    def __init__(self):
        self.sel_pos = 0
        self.actions = ["Play", "Generate", "Solve", "Quit"]

    def on_keypress(self, key: pynput.keyboard.Key):
        if key == pynput.keyboard.Key.enter:
            return False
        if key == pynput.keyboard.Key.up:
            self.sel_pos -= 1
            self.sel_pos %= len(self.actions)
            self.draw()
        if key == pynput.keyboard.Key.down:
            self.sel_pos += 1
            self.sel_pos %= len(self.actions)
            self.draw()
        return True

    def draw(self):
        subprocess.call("cls", shell=True)
        print(Fore.BLUE + """\
  ▄▄▄▄             █         █             ▄▄▄▄▄           ▄      ▄   
 █▀   ▀ ▄   ▄   ▄▄▄█   ▄▄▄   █   ▄  ▄   ▄  █    █  ▄▄▄   ▄▄█▄▄    █   
 ▀█▄▄▄  █   █  █▀ ▀█  █▀ ▀█  █ ▄▀   █   █  █▄▄▄▄▀ █▀ ▀█    █      █   
     ▀█ █   █  █   █  █   █  █▀█    █   █  █    █ █   █    █      ▀   
 ▀▄▄▄█▀ ▀▄▄▀█  ▀█▄██  ▀█▄█▀  █  ▀▄  ▀▄▄▀█  █▄▄▄▄▀ ▀█▄█▀    ▀▄▄    █   
 """ + Fore.RESET)
        print("======================================================================\n")
        for index, opt in enumerate(self.actions):
            if index == self.sel_pos:
                print(Fore.BLUE, end="")
            print(f"> {opt}")
            print(Fore.RESET)



class InteractiveBoard:
    def __init__(self, board: Board):
        self.select_row = 0
        self.select_col = 0

        self.board = board

    def draw(self):
        subprocess.call("cls", shell=True)
        print(self.board.find_valid_numbers(self.select_row, self.select_col))
        print("╔═╤═╤═╦═╤═╤═╦═╤═╤═╗")
        for i in range(9):
            print("║", end="")
            for j in range(9):
                if self.select_row == i and self.select_col == j:
                    print(Fore.BLUE + Back.WHITE, end="")
                if self.board.data[i][j] and self.board.data[i][j] not in self.board.find_valid_numbers(i, j):
                    print(Fore.RED, end="")
                print(self.board.data[i][j] if self.board.data[i][j] else " ", end="")
                print(Fore.RESET + Back.RESET, end="")
                print("║" if not (j + 1) % 3 else "│", end="")
            print("")
            if i < 8:
                print("╠═╪═╪═╬═╪═╪═╬═╪═╪═╣" if not (i + 1) % 3 else "╟─┼─┼─╫─┼─┼─╫─┼─┼─╢")
        print("╚═╧═╧═╩═╧═╧═╩═╧═╧═╝")


class InteractiveSolveBoard(InteractiveBoard):
    def on_keypress(self, key: pynput.keyboard.Key):
        if key == pynput.keyboard.Key.up:
            self.select_row -= 1
        if key == pynput.keyboard.Key.down:
            self.select_row += 1
        if key == pynput.keyboard.Key.left:
            self.select_col -= 1
        if key == pynput.keyboard.Key.right:
            self.select_col += 1
        self.select_row %= 9
        self.select_col %= 9
        if key == pynput.keyboard.Key.backspace:
            self.board.data[self.select_row][self.select_col] = 0
        try:
            if key.char.isdigit() and key.char != "0":
                self.board.data[self.select_row][self.select_col] = int(key.char)
        except AttributeError:
            pass
        self.draw()


