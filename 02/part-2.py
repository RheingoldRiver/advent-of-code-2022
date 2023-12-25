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
        'A X': 0 + 3,
        'B X': 0 + 1,
        'C X': 0 + 2,

        'A Y': 3 + 1,
        'B Y': 3 + 2,
        'C Y': 3 + 3,

        'A Z': 6 + 2,
        'B Z': 6 + 3,
        'C Z': 6 + 1,
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
