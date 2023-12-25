import json
import re
from collections import defaultdict
from copy import copy, deepcopy

from utils.aoc_entity import AOCEntity
from utils.parser.parser import Parser


class Entity(AOCEntity):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Solver:

    def __init__(self):
        with open('input.json', 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        self.lookup = {}
        self.crates = [[Parser.remove_many(x, '[] ') for x in Parser.split_into_equal_segments(
                s, 4)]
            for s in Parser.lines(self.data['crates'])
                       ]
        self.instructions = Parser.lines(self.data['instructions'])

    def build_crates(self):
        for crate in self.crates:
            for i, val in enumerate(crate):
                if val.strip() == "":
                    continue
                if i+1 not in self.lookup.keys():
                    self.lookup[i+1] = []
                self.lookup[i + 1].append(val)

    def run(self):
        self.build_crates()
        print(self.lookup)
        for insr in self.instructions:
            match = re.match(r"move (\d+) from (\d+) to (\d+)", insr)
            n = match[1]
            f = match[2]
            t = match[3]
            for _ in range(int(n)):
                box = self.lookup[int(f)].pop(0)
                self.lookup[int(t)].insert(0, box)
        x = []
        for c in range(1, len(self.lookup) + 1):
            x.append(self.lookup[c][0])
        print (''.join(x))


if __name__ == '__main__':
    print(Solver().run())
