import time
from Solver_CLI import solve

times = {}
files = 'sudoku_easy sudoku_medium sudoku_hard'.split()  # sudoku_17

for file in files:
    speed = []
    with open(file) as f:
        puzzles = f.readlines()

    for puzzle in puzzles:
        start = time.time()
        solve(puzzle.strip(), '0')
        end = time.time()
        # print(f"completed - {end-start}")

        speed.append(end-start)

    times[file] = speed
    print(f"file - {file}, avg - {sum(speed)/len(speed)}, max - {max(speed)}")
