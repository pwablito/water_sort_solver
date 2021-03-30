#!/usr/bin/env python3

from puzzle_solver import PuzzleSolver
from tube import Tube
from puzzle import Puzzle
import argparse


def strings_to_puzzle_horizontal(strings):
    tubes = []
    for row in strings:
        tube_layers = []
        for letter in row.strip("\n"):
            tube_layers.append(letter)
        tubes.append(Tube(tube_layers))
    return Puzzle(tubes)

def strings_to_puzzle_vertical(strings):
    flipped_strings = []
    for _ in range(len(strings[0])):
        flipped_strings.append("")
    for string in strings:
        for i in range(len(string)):
            if string[i] != " ":
                flipped_strings[i] += string[i]
    return strings_to_puzzle_horizontal(flipped_strings)

def main():
    parser = argparse.ArgumentParser("Solver for the WaterSortPuzzle iOS app")
    parser.add_argument("-i", "--input-file", required=True, type=str, help="File name to read puzzle from")
    parser.add_argument("-v", "--vertical", dest='vertical', action='store_true', help="Input file tubes are vertical")
    args = parser.parse_args()
    puzzle = None
    try:
        lines = open(args.input_file).readlines()
    except Exception:
        exit("Invalid input file")
    puzzle = strings_to_puzzle_vertical(lines) if args.vertical else strings_to_puzzle_horizontal(lines)
    solution = PuzzleSolver(puzzle).solve()
    if solution:
        for move in solution:
            print(move)
    else:
        print("Couldn't solve")


if __name__ == "__main__":
    main()
