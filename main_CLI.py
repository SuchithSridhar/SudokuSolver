'''
Author: SuchithSridhar
program: CLI sudoku solver
note: A gui version available, run main.py
choose puzzle in puzzlechoice.py
'''

from src.sudokuBoard import Board
from src.sudokuSolver import Solver
from src.puzzleChoice import choose
from tests import speedtest
import time
import sys


def solve(puzzle, blank="."):
    board = Board(puzzle, blank=blank)
    solver = Solver(board)
    solver.solve()


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "test":
        speedtest.main()
    else:
        puzzle, blank = choose()
        board = Board(puzzle, blank=blank)
        print(board)

        solver = Solver(board)
        start = time.time()
        solver.solve()
        end = time.time()

        print(board)
        print(f"Time taken = {end-start} seconds")
