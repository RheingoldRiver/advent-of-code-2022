import json
import re
from copy import copy, deepcopy

from utils.aoc_entity import AOCEntity


class Entity(AOCEntity):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Solver:

    def __init__(self):
        with open('input.txt', 'r', encoding='utf-8') as f:
            self.lines = [line.strip() for line in f.readlines()]

    def run(self):
        total = 0
        found = []
        for i, char in enumerate(self.lines[0]):
            if i < 14:
                found.append(char)
                continue
            found.pop(0)
            found.append(char)
            print(found)
            if len(set(found)) == 14:
                total = i + 1
                break


        return total


if __name__ == '__main__':
    print(Solver().run())
