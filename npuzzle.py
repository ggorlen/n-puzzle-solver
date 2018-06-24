"""
resources:

- https://algorithmsinsight.wordpress.com/graph-theory-2/implementing-bfs-for-pattern-database/
- https://algorithmsinsight.wordpress.com/graph-theory-2/a-star-in-general/implementing-a-star-to-solve-n-puzzle/
- http://www.cs.princeton.edu/courses/archive/spr10/cos226/assignments/8puzzle.html
- https://courses.cs.washington.edu/courses/cse473/12sp/slides/04-heuristics.pdf
- https://stackoverflow.com/questions/15947824/disjoint-pattern-database-for-15-puzzle
- https://www.cs.cf.ac.uk/PATS2/@archive_file?p=212&n=final&f=1-Andrew_Taylor__C0719820__Dissertation.pdf
- https://codereview.stackexchange.com/questions/33473/solving-15-puzzle
- https://heuristicswiki.wikispaces.com/file/view/Searching%20with%20pattern%20database%20%28Culberson%20%26%20Schaeffer%201996%29.pdf/92790472/Searching%20with%20pattern%20database%20%28Culberson%20%26%20Schaeffer%201996%29.pdf
- https://github.com/ivanwolf15/ida-star-python/
"""

import sys
import time
from astar import AStar
from idastar import IDAStar
from board import Board


class NPuzzle:
    def __init__(self, size=4, randomness=1000, board=None):
        self.board = Board(size, randomness, board)

    def play(self):
        while not self.board.finished():
            print(self.board)
            self.board.move(input("udlr:  "))

    def solve(self):
        solver = IDAStar()
        start = time.time()
        path = solver.search(self.board, Board(self.board.side))
        end = time.time()
        print("solution ({} moves, found in {} seconds):".format(len(path), round(end - start, 2)))
        [print(p) for p in path]


if __name__ == "__main__":
    board = [ 
        8, 3, 14, 10,
        2, 5, 13, 0,
        1, 6, 15, 11,
        9, 4, 7, 12
    ]
    board = [
        0, 1, 5,
        7, 4, 2,
        3, 8, 6
    ]
    board = [
        0, 2, 5,
        4, 6, 7,
        1, 3, 8
    ]
    puzzle = NPuzzle(3, 800, board)
    print("original puzzle:")
    print(puzzle.board)
    puzzle.solve()
