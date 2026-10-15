import board, solver, generator, ui

import colorama, pynput, subprocess

def menu_solve():
    b = ui.InteractiveSolveBoard(board.Board())

    b.draw()

    with pynput.keyboard.Listener(on_press=lambda key: b.on_keypress(key)) as listener:
        listener.join()

    subprocess.call("cls", shell=True)

    if not b.board.check_valid():
        print("Illegal board")
    else:
        solved = solver.solve(b.board)

        if solved:
            solved.pretty_print()
        else:
            print("No solution found")

    print("\nPress any key to exit...")
    with pynput.keyboard.Listener(on_press=lambda key: False) as listener:
        listener.join()


if __name__ == "__main__":
    colorama.init()

    sel = ui.ActionSelector()

    sel.draw()

    with pynput.keyboard.Listener(on_press = lambda key: sel.on_keypress(key)) as listener:
        listener.join()

    if sel.sel_pos == 3:
        exit(0)
    if sel.sel_pos == 2:
        menu_solve()

