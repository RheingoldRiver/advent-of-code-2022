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
        ptrs = []
        for i in range(1, 10):
            ptrs.append(grid.new_pointer('T' if i == 9 else str(i)))
        cur_head = grid.new_pointer('H')
        cur_head.update_value('T')
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
                cur_ptr = cur_head
                for next_ptr in ptrs:
                    if cur_ptr.horizontal_dist(next_ptr) > 1 or cur_ptr.vertical_dist(next_ptr) > 1:
                        next_ptr.move_in_direction_of(cur_ptr)
                    if next_ptr.id == 'T':
                        next_ptr.update_value('T')
                    cur_ptr = next_ptr

        return len(list(grid.grid_cells_with_value('T')))


if __name__ == '__main__':
    print(Solver().run())
