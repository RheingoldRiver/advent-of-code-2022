import json
import re
from copy import copy, deepcopy

from utils.aoc_entity import AOCEntity
from utils.grid.cell import Cell
from utils.grid.grid import Grid


class Entity(AOCEntity):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Solver:

    def __init__(self):
        with open('input.txt', 'r', encoding='utf-8') as f:
            self.lines = [line.strip() for line in f.readlines()]
        self.grid = Grid.read_from_lines(self.lines)

    def run(self):
        total = 0
        print('row forward')
        for row in self.grid.all_rows():
            cur_max = -1
            for cell in row:
                if (x := int(cell.value)) > cur_max:
                    if not cell.data.get('found'):
                        total += 1
                    cell.data['found'] = True
                    cur_max = x
        print(total)
        print('row backward')
        for row in self.grid.all_rows():
            cur_max = -1
            for cell in row.reversed():
                if (x := int(cell.value)) > cur_max:
                    if not cell.data.get('found'):
                        total += 1
                    cell.data['found'] = True
                    cur_max = x
        print(total)
        print('col down')
        for row in self.grid.all_columns():
            cur_max = -1
            for cell in row:
                if (x := int(cell.value)) > cur_max:
                    if not cell.data.get('found'):
                        total += 1
                    cell.data['found'] = True
                    cur_max = x
        print(total)
        print('col up')
        for row in self.grid.all_columns():
            cur_max = -1
            for cell in row.reversed():
                if (x := int(cell.value)) > cur_max:
                    if not cell.data.get('found'):
                        total += 1
                    cell.data['found'] = True
                    cur_max = x
        print(total)

        return total


if __name__ == '__main__':
    print(Solver().run())
