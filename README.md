# SudokuBot - a small TUI sudoku generator and solver

## Features:

- Generating (pseudo) random sudoku puzzle boards of varying difficulty
- - each one only having one unique solution
- Allowing the user to play those boards in the app itself via an interactive environment, as well as to copy-paste them to use elsewhere
- Solving any given sudoku board (as long as a solution exists!)

## Setting up:

### Main:

To set up, please run the following commands:

```
git clone https://github.com/azazel-261/SudokuBot/
cd SudokuBot
pip install -r requirements.txt
```
Once done, simply run `python main.py` (or `python3 main.py` for some OSX/UNIX users)

### Optional command line arguments:

While running without arguments will always get you to the TUI, you can use, the following arguments can be supplied to alter the program's functionality in different ways: 

- `-g / --generate [easy, medium, hard]` - use to generate a sudoku board directly to stdout instead of entering TUI. Example usage: `python main.py -g easy`
- `-s / --solve [BOARD]` - use to solve a board without entering TUI, the solved board will be printed to stdout. Example usage: `python main.py --solve 123...4_6`
- `-r / --raw` - use in combination with the two arguments above to receive just the raw board data without the fancy formatting. Example: `python main.py -r --generate medium`
- `--igenerate` - use to enter the interactive generator without using the initial TUI selector
- `--isolve` - same thing, use it to start solving a bit faster!
- `--play` - skip the selector and go straight into the interactive playing board!
- `-h / --help` - read all the same instructions again but in your terminal




