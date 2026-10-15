import sys, argparse

import board, solver, generator, ui

import colorama, pynput, subprocess

def menu_solve():
    interactive = ui.InteractiveSolveBoard(board.Board())

    interactive.draw()

    with pynput.keyboard.Listener(on_press=lambda key: interactive.on_keypress(key)) as listener:
        listener.join()

    subprocess.call("cls", shell=True)

    if not interactive.board.check_valid():
        print("Illegal board")
    else:
        solved = solver.solve(interactive.board)

        if solved:
            solved.pretty_print()
        else:
            print("No solution found")

    print("\nPress any key to exit...")
    with pynput.keyboard.Listener(on_press=lambda key: False) as listener:
        listener.join()


def menu_play():
    difficulty_sel = ui.DifficultySelector()

    difficulty_sel.draw()

    with pynput.keyboard.Listener(on_press=lambda key: difficulty_sel.on_keypress(key)) as listener:
        listener.join()

    subprocess.call("cls", shell=True)

    remove = [25, 40, 55][difficulty_sel.difficulty]

    print("Generating...")

    s_board = generator.generate_solved()
    u_board = generator.unsolve(s_board, remove)

    player = ui.InteractivePlayBoard(u_board)

    player.draw()

    with pynput.keyboard.Listener(on_press=lambda key: player.on_keypress(key)) as listener:
        listener.join()

    subprocess.call("cls", shell=True)

    print("Good job!\n")
    print("Press any key to exit...")
    with pynput.keyboard.Listener(on_press=lambda key: False) as listener:
        listener.join()


def menu_generate():
    difficulty_sel = ui.DifficultySelector()

    difficulty_sel.draw()

    with pynput.keyboard.Listener(on_press=lambda key: difficulty_sel.on_keypress(key)) as listener:
        listener.join()

    subprocess.call("cls", shell=True)

    remove = [25, 40, 55][difficulty_sel.difficulty]

    print("Generating...")

    s_board = generator.generate_solved()
    u_board = generator.unsolve(s_board, remove)

    subprocess.call("cls", shell=True)

    u_board.pretty_print()

    print("Press any key to exit...")
    with pynput.keyboard.Listener(on_press=lambda key: False) as listener:
        listener.join()


def menu():
    sel = ui.ActionSelector()

    sel.draw()

    with pynput.keyboard.Listener(on_press=lambda key: sel.on_keypress(key)) as listener:
        listener.join()

    if sel.sel_pos == 3:
        exit(0)
    if sel.sel_pos == 2:
        menu_solve()
    if sel.sel_pos == 1:
        menu_generate()
    if sel.sel_pos == 0:
        menu_play()


if __name__ == "__main__":
    colorama.init()

    parser = argparse.ArgumentParser(prog='main.py', description='Pass no arguments to use the interactive menu')

    parser.add_argument('-r', '--raw',
                        action='store_true',
                        help='Use this flag to make the app return the raw result without the fancy borders. Only works outside of TUI')

    parser.add_argument('-s', '--solve',
                        help='Stand for interactive-solve. Use this flag to pass in an unsolved sudoku board as raw data (left to right, top to bottom, 0 or _ instead of empty fields)')
    parser.add_argument('--isolve',
                        action='store_true',
                        help='Use this flag to pass your unsolved board via the fancy TUI')

    parser.add_argument('-g', '--generate',
                        help='Use this to generate a puzzle outside of the TUI. Pass the difficulty',
                        choices=['easy', 'medium', 'hard'])
    parser.add_argument('--igenerate',
                        action='store_true',
                        help='This flag is used to generate in the interactive TUI')

    parser.add_argument('-p', '--play',
                        action='store_true',
                        help='Generate a board for you to attempt to solve, all within the fancy TUI')

    args = parser.parse_args(sys.argv[1:])

    if args.solve:
        unsolved = board.Board()

        try:
            for i in range(81):
                if args.solve[i] == '_':
                    unsolved.data[i // 9][i % 9] = 0
                else:
                    unsolved.data[i // 9][i % 9] = int(args.solve[i])
        except IndexError, ValueError:
            print("Ill-formed board data")
            exit(1)

        if not unsolved.check_valid():
            print("Illegal board")
            exit(2)

        if args.raw:
            solver.solve(unsolved).print()
        else:
            solver.solve(unsolved).pretty_print()
        exit(0)

    if args.isolve:
        menu_solve()
        exit(0)

    if args.generate:
        remove = {
            "easy" : 25,
            "medium" : 40,
            "hard" : 55
        }[args.generate]

        s_board = generator.generate_solved()
        u_board = generator.unsolve(s_board, remove)

        if args.raw:
            u_board.print()
        else:
            u_board.pretty_print()
        exit(0)

    if args.igenerate:
        menu_generate()
        exit(0)

    if args.play:
        menu_play()
        exit(0)

    menu()

