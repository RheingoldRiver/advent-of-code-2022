import json
import re
from copy import copy, deepcopy
from itertools import product

from utils.aoc_entity import AOCEntity
from utils.grid.cell import Cell
from utils.grid.grid import Grid
from utils.grid.pointer import Pointer


class Entity(AOCEntity):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Solver:

    def __init__(self):
        with open('input.txt', 'r', encoding='utf-8') as f:
            self.lines = [line.strip() for line in f.readlines()]
        self.grid = Grid.read_from_lines(self.lines)

    def run(self):
        max_poss = 0
        for cell in self.grid.all_grid_cells():
            cell.set_value(int(cell.value))
        grid = self.grid
        ptr = grid.new_pointer()
        for cell in self.grid.all_grid_cells():
            if cell.row == 0 or cell.row == self.grid.max_row:
                continue
            if cell.col == 0 or cell.col == self.grid.max_col:
                continue
            ptr.move_to(cell.row, cell.col)
            cells_above = ptr.cells_above()
            cells_above.reverse()
            cells_below = ptr.cells_below()
            cells_left = ptr.cells_to_left()
            cells_left.reverse()
            cells_right = ptr.cells_to_right()
            trees = []
            trees.append(self.count_in_range(cells_above, ptr))
            trees.append(self.count_in_range(cells_below, ptr))
            trees.append(self.count_in_range(cells_left, ptr))
            if all([tree == 1 for tree in trees]):
                continue
            trees.append(self.count_in_range(cells_right, ptr))
            prod = trees[0] * trees[1] * trees[2] * trees[3]
            max_poss = max(max_poss, prod)

        return max_poss

    def count_in_range(self, row, ptr: Pointer):
        total = 0
        for cell in row:
            total += 1
            if cell.value >= ptr.value:
                return total
        return total


if __name__ == '__main__':
    print(Solver().run())
