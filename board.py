import copy
import random


class Board:
    def __init__(self, side=4, randomness=1000, board=None):
        self.side = side
        self.board = list(range(1, side * side))
        self.board.append(0)
        self.goal = copy.deepcopy(self.board)
        self.blank_idx = len(self.board) - 1
        self.previous_board = None
        self.ply = 0

        for _ in range(randomness):
            self.move(random.choice(self.get_moves()), False)

        # reset ply to 0
        self.ply = 0

    def finished(self):
        """ 
        returns true if the board is complete
        """
        return self.board == self.goal

    def misplaced_count(self):
        """ 
        counts the number of squares not in 
        their final location on the board
        """
        misplaced = 0
        
        for i in range(len(self.board) - 1):
            if self.board[i] != i + 1:
                misplaced += 1
            
        return misplaced

    def get_neighbors(self):
        """ 
        returns a list of positions that can be reached
        through a valid move on the board, ignoring the
        board's previous position to avoid loops
        """
        neighbors = []

        for direction in self.get_moves():
            board_copy = copy.deepcopy(self)
            board_copy.move(direction, False)

            if board_copy.board != self.previous_board:
                neighbors.append(board_copy)

        return neighbors

    def get_moves(self):
        """ 
        returns a list of valid moves for the current board
        """
        moves = []
        
        if self.blank_idx > self.side - 1:
            moves.append("d")
        
        if self.blank_idx < len(self.board) - self.side:
            moves.append("u")

        if self.blank_idx % self.side > 0:
            moves.append("r")

        if self.blank_idx % self.side < self.side - 1:
            moves.append("l")

        return moves
        
    def move(self, direction, validate=True):
        """ 
        moves a square into the empty space if possible
        """

        if validate and direction not in self.get_moves():
            return False

        self.ply += 1
        self.previous_board = copy.deepcopy(self.board)
            
        if direction == "d":
            self._swap_with_blank(self.blank_idx - self.side)
        elif direction == "u":
            self._swap_with_blank(self.blank_idx + self.side)
        elif direction == "r":
            self._swap_with_blank(self.blank_idx - 1)
        else: # direction == "l":
            self._swap_with_blank(self.blank_idx + 1)

        return True
        
    def _swap_with_blank(self, dest_idx):
        self.board[self.blank_idx] = self.board[dest_idx]
        self.board[dest_idx] = 0
        self.blank_idx = dest_idx

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def __lt__(self, other):
        """ 
        hamming priority
        """
        return self.ply + self.misplaced_count() < other.ply + other.misplaced_count()

    def __str__(self):
        b = ["\n\n     "]

        for i in range(len(self.board)):
            if self.board[i]:
                b.append(str(self.board[i]).ljust(3) )
            else:
                b.append("_".ljust(3))
            
            if i % self.side == self.side - 1:
                b.append("\n\n     ")
        
        return "".join(b)
