class Board:

    def __init__(self, text, blank="0"):
        self.board = []
        blank = str(blank)
        row = 0
        col = 0
        temp = []
        for item in text:

            if item == blank:
                node = Node(0, (row, col), fixed=False)
            else:
                node = Node(int(item), (row, col), fixed=True)

            col += 1
            temp.append(node)

            if col == 9:
                col = 0
                row += 1
                self.board.append(temp)
                temp = []

    def __repr__(self):
        return self.stringrep()

    def __str__(self):
        return self.stringrep()

    def stringrep(self):
        horz_sep = ""
        horz_sep_2 = "-"
        vert_sep = ""
        vert_sep_2 = "|"
        col_no = (10+(9*2)+2)
        string = ""

        for row in self.board:

            if row[0].row in (3, 6):
                string += horz_sep_2 * col_no
            else:
                string += horz_sep * col_no
            string += "\n"

            for col in row:

                if col.col in (3, 6):
                    string += vert_sep_2
                else:
                    string += vert_sep

                string += f" {str(col)} "

            string += vert_sep
            string += "\n"

        string += horz_sep * col_no

        return string

    def change_value(self, row, col, new_value):
        self.board[row][col].update(int(new_value))

    def get_value(self, row, col):
        return self.board[row][col]


class Node:

    def __init__(self, number, position, fixed=False):
        self.number = number
        self.row, self.col = position
        self.fixed = fixed
        if not fixed:
            self.possible = set([x for x in range(1, 10)])
        else:
            self.possible = set()

    def __repr__(self):
        if self.number == 0:
            return " "

        return str(self.number)

    def __str__(self):
        if self.number == 0:
            return " "

        return str(self.number)

    def update(self, num):
        self.number = num
