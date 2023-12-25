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
            if pair['elf1']['min'] >= pair['elf2']['min'] and pair['elf1']['max'] <= pair['elf2']['max']:
                count += 1
                print(f'{str(pair["elf1"])} {str(pair["elf2"])}')
            elif pair['elf2']['min'] >= pair['elf1']['min'] and pair['elf2']['max'] <= pair['elf1']['max']:
                print(f'{str(pair["elf2"])} {str(pair["elf1"])}')
                count += 1
        return count


if __name__ == '__main__':
    print(Solver().run())
