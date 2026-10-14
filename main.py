import board, solver, generator, ui

import colorama, pynput

if __name__ == "__main__":
    colorama.init()

    sel = ui.ActionSelector()

    sel.draw()

    with pynput.keyboard.Listener(on_press = lambda key: sel.on_keypress(key)) as listener:
        listener.join()

    if sel.sel_pos == 3:
        exit(0)

    b = ui.InteractiveSolveBoard(board.Board())

    b.draw()

    with pynput.keyboard.Listener(on_press = lambda key: b.on_keypress(key)) as listener:
        listener.join()

