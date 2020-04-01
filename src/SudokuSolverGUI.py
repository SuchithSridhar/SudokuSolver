from .sudokuBoard import Board
from .sudokuSolver import Solver
from .puzzleChoice import choose
import tkinter as tk
from time import sleep, time


def main():
    puzzle, blank = choose()
    board = Board(puzzle, blank=blank)

    solver = Solver(board)
    flat = solver.flat

    root = tk.Tk()
    frame = tk.Frame(root)
    canvas = tk.Canvas(frame)
    frame.place(x=0, y=0, w=630, h=635)
    canvas.place(x=0, y=0, w=630, h=635)

    count = 0
    for i in range(7, 63, 7):
        if count in (2, 5):
            width = 3
        else:
            width = 0
        canvas.create_line(i*10, 0, i*10, 630, width=width)
        canvas.create_line(0, i*10, 630, i*10, width=width)

        count += 1

    x = 0
    y = 0
    pad = 10

    def changeNode(node, value):
        if value != 0:
            node.var.set(str(value))
        else:
            node.var.set(" ")
        x = float(entry.get())
        sleep(x)
        try:
            root.update()
        except Exception:
            pass

    def buttonCall():
        size = entry.get()

    for node in flat:
        var = tk.StringVar()
        label = tk.Label(frame, textvariable=var, font=("CourierBold", 20))
        node.var = var
        var.set(str(node))
        label.place(x=x+pad, y=y+pad, w=60-pad, h=60-pad)
        x += 70
        if x == 630:
            x = 0
            y += 70

    canvas.create_line(0, 630, 630, 630, width=3)

    label = tk.Label(root, text="Sleep:")
    label.place(x=420, y=640, h=50)

    entry = tk.StringVar()
    entry.set("0.5")
    tk.Entry(root, textvariable=entry).place(x=480, y=650, w=100, h=30)

    button = tk.Button(root, text="Solve",
                       command=lambda: solver.solve(changeNode))
    button.place(x=20, y=640, w=100, h=50)

    root.geometry("630x700")
    root.mainloop()


if __name__ == "__main__":
    main()
