"""
http://www.cs.princeton.edu/courses/archive/spr10/cos226/assignments/8puzzle.html
"""

import sys
import time
from astar import AStar
from board import Board


class NPuzzle:
    def __init__(self, size=4, randomness=1000):
        self.board = Board(size, randomness)

    def play(self):
        while not self.board.finished():
            print(self.board)
            self.board.move(input("udlr:  "))

    def solve(self):
        solver = AStar()
        start = time.time()
        path = solver.search(self.board, Board(self.board.side, 0))
        end = time.time()
        print("solution ({} moves, found in {} seconds):".format(len(path), round(end - start, 2)))
        [print(p) for p in path]


if __name__ == "__main__":
    puzzle = NPuzzle(3, 6000)
    print("original puzzle:")
    print(puzzle.board)
    puzzle.solve()
