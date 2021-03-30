from copy import deepcopy
from puzzle import Puzzle
from move import Move
from errors import MovesExpendedException

class PuzzleSolver:

    def __init__(self, puzzle):
        self.puzzle = puzzle

    def solve(self):
        solution = []
        return PuzzleSolver.static_solve(self.puzzle, solution)

    @staticmethod
    def static_solve(puzzle, solution):
        if puzzle.is_solved():
            return solution
        move = None
        while True:
            try:
                avoid = None
                if len(solution) != 0:
                    avoid = solution[len(solution) - 1]
                move = PuzzleSolver.get_next_move(puzzle, move, avoid=avoid)
                if puzzle.can_move(move):
                    test_puzzle = deepcopy(puzzle)
                    test_solution = deepcopy(solution)
                    test_puzzle.move(move)
                    test_solution.append(move)
                    returned_solution = PuzzleSolver.static_solve(test_puzzle, test_solution)
                    if returned_solution is not None:
                        return returned_solution
                    # Dead end, try next possible move
            except MovesExpendedException:
                break
        return None

    @staticmethod
    def get_next_move(puzzle, last_move, avoid=None):
        def next_move(last):
            source = last.source
            target = last.target
            if target == len(puzzle.tubes) - 1:
                target = 0
                if source == len(puzzle.tubes) - 1:
                    raise MovesExpendedException()
                else:
                    source += 1
            else:
                target += 1
            return Move(source, target)
        move = last_move
        if move is None:
            move = Move(0, 0)
        while True:
            move = next_move(move)
            if move.source != move.target:
                if avoid is not None:
                    if move.source != avoid.target or move.target != avoid.source:
                        return move
                else:
                    return move