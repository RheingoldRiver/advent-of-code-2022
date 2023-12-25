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
        total = 0
        for line in self.lines:
            word = list(line)
            p1 = line[:int(len(word)/2)]
            p2 = line[int(len(word)/2):]
            print(p2)
            for char in p1:
                if char in p2:
                    print(f"{char} {self.get_val(char)}")
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
