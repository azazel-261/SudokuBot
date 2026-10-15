import sys

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

    if len(sys.argv) < 2:
        menu()
    elif sys.argv[1] == "menu":
        menu()
    elif sys.argv[1] == "play":
        menu_play()
    elif sys.argv[1] == "solve":
        menu_solve()
    elif sys.argv[1] == "generate":
        menu_generate()