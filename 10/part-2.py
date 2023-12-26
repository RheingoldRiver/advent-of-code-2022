import json
import re
from copy import copy, deepcopy

from utils.aoc_entity import AOCEntity
from utils.parser.parser import Parser


class Entity(AOCEntity):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Solver:

    def __init__(self):
        with open('input.txt', 'r', encoding='utf-8') as f:
            self.lines = [line.strip() for line in f.readlines()]

    def run(self):
        total = 0
        x = 1
        j = 0
        interesting = {
            20: False,
            60: False,
            100: False,
            140: False,
            180: False,
            220: False,
        }
        rows = []
        current_row = list('.' * 300)
        sprite_range = range(0, 2)

        def update_sprite(index, allowed_range):
            if index % 40 in allowed_range:
                current_row[index] = '#'
            else:
                current_row[index] = '.'

        for line in self.lines:
            if j in interesting:
                rows.append(copy(current_row))
            if line == 'noop':
                update_sprite(j, sprite_range)
                j += 1
                continue
            update_sprite(j, sprite_range)
            j += 1
            if j in interesting:
                rows.append(copy(current_row))
            update_sprite(j, sprite_range)
            j += 1
            x = x + int(line.replace('addx ', ''))
            sprite_range = range(max(0, x - 1), min(39, x + 2))
        print('\n'.join(''.join(x) for x in Parser.split_into_equal_segments(''.join(current_row), 40)))
        return total

    def update_queue(self, queue):
        total = 0
        done = []
        for task in queue:
            if task['time'] > 1:
                task['time'] = task['time'] - 1
            else:
                done.append(task)
                total += task['value']
        for task in done:
            queue.remove(task)
        return total


if __name__ == '__main__':
    print(Solver().run())
