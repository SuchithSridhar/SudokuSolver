class Solver:

    def __init__(self, board):

        self.boardObj = board
        self.board = board.board
        self.flat = []
        self.stack = []

        for row in self.board:
            self.flat += row

        self.nodes = [x for x in self.flat if not x.fixed]
        self.nodeslen = len(self.nodes)

    def solve(self, changing_value_function=None):
        if self.stack == []:
            self.stack.append(self.nodes[0])

        if changing_value_function is None:
            def changing_value_function(node, value): return None

        current_item = 0
        back_track = False
        while True:
            value = self.pick_value(self.stack[-1], back_track=back_track)
            if not value:
                current_item -= 1
                if self.stack == []:
                    return False
                node = self.stack.pop()

                # Useful for GUI
                changing_value_function(node, value)
                node.update(0)
                back_track = True
            else:
                current_item += 1
                changing_value_function(self.stack[-1], value)
                self.stack[-1].update(value)
                self.stack[-1].possible = self.stack[-1].possible - {value}

                if current_item == self.nodeslen:
                    return True
                self.stack.append(self.nodes[current_item])

                back_track = False

    def pick_value(self, node, back_track):
        if not back_track:
            node.possible = self.calc_possible(node)

        if node.possible == set():
            return 0

        return list(node.possible)[0]

    def calc_possible(self, node):
        possible = set([x for x in range(1, 10)])

        # Remove ones in the same row
        completed = (x.number for x in self.board[node.row])

        possible = possible - set(completed)

        # Remove ones in same column
        completed = set([self.board[i][node.col].number for i in range(9)])
        possible = possible - set(completed)

        # Remove within square
        box_x = (node.row//3) * 3
        box_y = (node.col//3) * 3
        # The above statements gives us the pos of the top
        # left element of the box our number belongs to
        completed = []
        for i in range(box_x, box_x+3):
            for j in range(box_y, box_y+3):
                completed.append(self.boardObj.get_value(i, j).number)

        possible = possible - set(completed)

        return possible
