import json
import re
from copy import copy, deepcopy


class Solver:
    A = 'Rock'
    B = 'Paper'
    C = 'Scissors'
    X = 'Rock'
    Y = 'Paper'
    Z = 'Scissors'
    scores = {
        'A Y': 6 + 2,
        'B Y': 3 + 2,
        'C Y': 0 + 2,
        'A X': 3 + 1,
        'B X': 0 + 1,
        'C X': 6 + 1,
        'A Z': 0 + 3,  # Rock Scissors
        'B Z': 6 + 3,  # Paper Scissors
        'C Z': 3 + 3,  # Scissors Scissors
    }

    def __init__(self):
        with open('input.txt', 'r', encoding='utf-8') as f:
            self.lines = [line.strip() for line in f.readlines()]

    def run(self):
        total = 0
        for line in self.lines:
            total += self.scores[line]

        return total


if __name__ == '__main__':
    print(Solver().run())
