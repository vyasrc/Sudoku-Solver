import tkinter as tk
import tkinter.messagebox
import threading
import numpy as np


class GUI(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        master.title("Sudoku")
        self.pack()
        self.array = np.array(self.make_board())
        np.put(self.array, np.random.choice(range(81), int(81 * 0.6), replace=False), 0)
        self.create_widgets()


    def create_widgets(self):
        self.buttons = {}
        x_pos = 0
        for row in self.array:
            y_pos = 0
            for val in row:
                button = tk.Button(self, width=6, height=3, text=val)
                button.grid(row=x_pos, column=y_pos)
                self.buttons[(x_pos, y_pos)] = button
                y_pos += 1
            x_pos += 1
        self.QUIT = tk.Button(self, text="QUIT", fg="red", width=6, height=3,
                              command=root.destroy).grid(row=x_pos-1, column=y_pos)

        self.FIND = tk.Button(self, text="FIND", fg="blue", width=6, height=3,
                              command=self.thread_func).grid(row=x_pos-2, column=y_pos)

    def thread_func(self):
        self.thread = threading.Thread(target=self.solve())
        self.thread.start()

    def solve(self):
        if self.solve_recursive():
            tkinter.messagebox.showinfo('Success', 'Solution Found')
        else:
            tkinter.messagebox.showinfo('Error', 'No Solution Found')

    def make_board(self, m=3):
        """Return a random filled m**2 x m**2 Sudoku board."""
        n = m ** 2
        board = [[None for _ in range(n)] for _ in range(n)]

        def search(c=0):
            "Recursively search for a solution starting at position c."
            i, j = divmod(c, n)
            i0, j0 = i - i % m, j - j % m  # Origin of mxm block
            numbers = list(range(1, n + 1))
            np.random.shuffle(numbers)
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

    def solve_recursive(self):
        try:
            find = tuple(np.argwhere(self.array == 0)[0])
        except:
            return True

        for i in range(1, 10):
            if self.is_valid(i, find):
                self.array[find[0]][find[1]] = i
                self.buttons[find]["text"] = i

                if self.solve_recursive():
                    return True

                self.array[find[0]][find[1]] = 0
                self.buttons[find]["text"] = 0

        return False

root = tk.Tk()
app = GUI(master=root)
app.mainloop()

