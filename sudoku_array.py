import numpy as np
import random


class Sudoku:
    def __init__(self):
        self.array = np.array(self.make_board())
        np.put(self.array, np.random.choice(range(81), int(81 * 0.6), replace=False), 0)


    def make_board(self, m=3):
        """Return a random filled m**2 x m**2 Sudoku board."""
        n = m ** 2
        board = [[None for _ in range(n)] for _ in range(n)]

        def search(c=0):
            "Recursively search for a solution starting at position c."
            i, j = divmod(c, n)
            i0, j0 = i - i % m, j - j % m  # Origin of mxm block
            numbers = list(range(1, n + 1))
            random.shuffle(numbers)
            for x in numbers:
                if (x not in board[i]  # row
                        and all(row[j] != x for row in board)  # column
                        and all(x not in row[j0:j0 + m]  # block
                                for row in board[i0:i])):
                    board[i][j] = x
                    if c + 1 >= n ** 2 or search(c + 1):
                        return board
            else:
                # No number is valid in this cell: backtrack and try again.
                board[i][j] = None
                return None

        return search()

    def is_valid(self, num, pos):
        if num in self.array[pos[0]] and np.argwhere(self.array[pos[0]] == num)[0][0] != pos[1]:
            return False

        if num in self.array[:9, pos[1]] and np.argwhere(self.array[:9, pos[1]] == num)[0][0] != pos[0]:
            return False

        x = (pos[1] // 3) * 3
        y = (pos[0] // 3) * 3

        if num in self.array[y: y + 3, x: x + 3] and \
            tuple(np.argwhere(self.array[y: y + 3, x: x + 3] == num)[0]) != pos:
            return False

        return True

    def solve(self):
        try:
            find = tuple(np.argwhere(self.array == 0)[0])
        except:
            return True

        for i in range(1, 10):
            if self.is_valid(i, find):
                self.array[find[0]][find[1]] = i

                if self.solve():
                    return True

                self.array[find[0]][find[1]] = 0

        return False


if __name__== "__main__":
    ob = Sudoku()
    print(ob.array)
    if ob.solve():
        print(ob.array)
    else:
        Print("Not Solved")
