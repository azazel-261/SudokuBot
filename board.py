class Board:
    def __init__(self):
        self.data = [[0 for __ in range(9)] for _ in range(9)]

    def find_valid_numbers(self, row: int, col: int):
        valid_numbers = set(range(1, 10))
        # Row
        for index, number in enumerate(self.data[row]):
            if index == col:
                continue
            if number:
                try:
                    valid_numbers.remove(number)
                except:
                    pass

        # Column
        for i in range(9):
            if i == row:
                continue
            number = self.data[i][col]
            if number:
                try:
                    valid_numbers.remove(number)
                except:
                    pass

        # Subgrid
        subgrid_row = row - (row % 3)
        subgrid_col = col - (col % 3)

        for i in range(3):
            for j in range(3):
                local_row = subgrid_row + i
                local_col = subgrid_col + j
                if local_row == row and local_col == col:
                    continue
                number = self.data[local_row][local_col]
                if number:
                    try:
                        valid_numbers.remove(number)
                    except:
                        pass
        return list(valid_numbers)

    def print(self):
        for i in range(9):
            if i and not i % 3:
                print("")
            for j in range(9):
                if j and not j % 3:
                    print(" ", end="")
                print(self.data[i][j] if self.data[i][j] else "_", end="")
            print("\n", end="")

    def pretty_print(self):
        print("╔═╤═╤═╦═╤═╤═╦═╤═╤═╗")
        for i in range(9):
            print("║", end="")
            for j in range(9):
                print(self.data[i][j] if self.data[i][j] else " ", end="")
                print("║" if not (j + 1) % 3 else "│", end="")
            print("")
            if i < 8:
                print("╠═╪═╪═╬═╪═╪═╬═╪═╪═╣" if not (i + 1) % 3 else "╟─┼─┼─╫─┼─┼─╫─┼─┼─╢")
        print("╚═╧═╧═╩═╧═╧═╩═╧═╧═╝")

    def check_valid(self):
        for i in range(9):
            for j in range(9):
                if self.data[i][j] and self.data[i][j] not in self.find_valid_numbers(i, j):
                    return False
        return True

    def check_solved(self):
        for i in range(9):
            for j in range(9):
                if self.data[i][j] not in self.find_valid_numbers(i, j):
                    return False
        return True
