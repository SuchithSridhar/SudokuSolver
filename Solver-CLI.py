'''
Author: SuchithSridhar
program: CLI sudoku solver
note: A gui version available, run main.py
choose puzzle in puzzlechoice.py
'''

from sudokuBoard import Board
from sudokuSolver import Solver
from puzzleChoice import choose
import time

puzzle, blank = choose()
board = Board(puzzle, blank=blank)
print(board)

solver = Solver(board)
start = time.time()
solver.solve()
end = time.time()

print(board)
print(f"Time taken = {end-start} seconds")
