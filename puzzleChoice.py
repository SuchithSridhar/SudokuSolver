def choose():
    with open("easy50.txt") as f:
        # Change the file up here to "hardest.txt" to try harder puzzles
        lines = f.readlines()

        # Change the index to change the puzzle
        line = lines[0].strip()

    # Blank param is for the area that are blank
    blank = '.'

    return line, blank
