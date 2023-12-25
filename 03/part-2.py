import json
import re
from copy import copy, deepcopy


class Solver:

    def __init__(self):
        with open('input.txt', 'r', encoding='utf-8') as f:
            self.lines = [line.strip() for line in f.readlines()]
        self.data = self.parse_lines()

    def parse_lines(self):
        data = []
        i = 0
        cur = []
        for line in self.lines:
            if i == 3:
                i = 1
                data.append(cur)
                cur = [line]
                continue
            cur.append(line)
            i += 1
        data.append(cur)
        print(data)
        return data

    def run(self):
        total = 0
        for group in self.data:
            for char in group[0]:
                if char in group[1] and char in group[2]:
                    total += self.get_val(char)
                    break
        return total

    @staticmethod
    def get_val(char):
        if char.isupper():
            return ord(char) - ord('A') + 27
        return ord(char) - ord('a') + 1


if __name__ == '__main__':
    print(Solver().run())
