import json
import re
from copy import copy, deepcopy


class Solver:

    def __init__(self):
        with open('input.txt', 'r', encoding='utf-8') as f:
            self.lines = [line.strip() for line in f.readlines()]
        self.data = self.process_data()

    def process_data(self):
        ret = []
        for line in self.lines:
            ret.append({
                "elf1": self.split_elf(line.split(',')[0]),
                "elf2": self.split_elf(line.split(',')[1])
            })
        return ret

    def split_elf(self, elf):
        return {
            'min': int(elf.split('-')[0]),
            'max': int(elf.split('-')[1]),
        }

    def run(self):
        count = 0
        for pair in self.data:
            cur_elf = pair['elf1']
            other_elf = pair['elf2']
            if other_elf['min'] <= cur_elf['max'] <= other_elf['max']:
                count += 1
                continue
            if other_elf['max'] >= cur_elf['min'] >= other_elf['min']:
                count += 1
                continue
            cur_elf = pair['elf2']
            other_elf = pair['elf1']
            if other_elf['min'] <= cur_elf['max'] <= other_elf['max']:
                count += 1
                continue
            if other_elf['max'] >= cur_elf['min'] >= other_elf['min']:
                count += 1
                continue
        return count


if __name__ == '__main__':
    print(Solver().run())
