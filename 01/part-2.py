import json
import re
from copy import copy, deepcopy


class Solver:

    def __init__(self):
        with open('input.txt', 'r', encoding='utf-8') as f:
            self.lines = [line.strip() for line in f.readlines()]
        # with open('info2.json', 'r', encoding='utf-8') as f:
        #     self.data = json.load(f)

    def run(self):
        amts = []
        current = 0
        for line in self.lines:
            if line == '':
                amts.append(current)
                current = 0
                continue
            current += int(line)
        amts.append(current)
        amts2 = sorted(amts)
        amts2.reverse()
        return amts2[0] + amts2[1] + amts2[2]


if __name__ == '__main__':
    print(Solver().run())
