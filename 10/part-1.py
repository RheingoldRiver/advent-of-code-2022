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
        x = 1
        j = 1
        interesting = {
            20: False,
            60: False,
            100: False,
            140: False,
            180: False,
            220: False,
        }
        for i, line in enumerate(self.lines):
            if j in interesting:
                print(x * j)
                total += x * j
                interesting[j] = True
            if line == 'noop':
                j += 1
                continue
            if j + 1 in interesting and interesting[j + 1] is False:
                print(x, j+1, x * (j + 1))
                total += x * (j + 1)
                interesting[j + 1] = True
            j += 2
            x = x + int(line.replace('addx ', ''))
        print(j)
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
