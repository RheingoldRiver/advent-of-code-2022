import json
import re
from copy import copy, deepcopy

from utils.grid import Grid


class Solver:

    def __init__(self):
        with open('input.txt', 'r', encoding='utf-8') as f:
            self.lines = [line.strip() for line in f.readlines()]

    def run(self):
        total = 0
        grid = Grid.empty_grid(1, 1)
        grid.set_infinite()
        cur_head = grid.new_pointer('H')
        cur_tail = grid.new_pointer('T')
        cur_tail.update_value('T')
        for line in self.lines:
            direction = line.split()[0]
            units = int(line.split()[1])
            print(line)
            for i in range(units):
                if direction == 'L':
                    cur_head.move_left(1)
                elif direction == 'R':
                    cur_head.move_right(1)
                elif direction == 'U':
                    cur_head.move_up(1)
                elif direction == 'D':
                    cur_head.move_down(1)
                if cur_head.vertical_dist(cur_tail) > 1 or cur_head.horizontal_dist(cur_tail) > 1:
                    cur_tail.move_in_direction_of(cur_head)
                    cur_tail.update_value('T')

        return len(list(grid.grid_cells_with_value('T')))


if __name__ == '__main__':
    print(Solver().run())
