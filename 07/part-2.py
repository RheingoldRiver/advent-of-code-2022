import json
import re
from copy import copy, deepcopy
from typing import List, Dict

from utils.aoc_entity import AOCEntity
from utils.parser.parser import Parser

all_folders = []


class Folder(AOCEntity):
    name: str
    parent: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.children = []
        self.size = 0

    def add_size(self, num):
        self.size += num

    def add_child(self, name):
        if name in self.children:
            return
        self.children.append(name)

    @property
    def children_names(self):
        return [x.name for x in self.children]

    def size_of_children(self):
        return self.size + sum([c.size_of_children() for c in self.children])

    def get_parent(self):
        return self.parent

    def child_by_key(self, key):
        for child in self.children:
            if child.name == key:
                return child


class Solver:

    def __init__(self):
        with open('input.txt', 'r', encoding='utf-8') as f:
            self.lines = [line.strip() for line in f.readlines()]
        self.lines.pop(0)  # ignore the /, we'll do that manually

    def run(self):
        total = 0
        root = Folder(name='root', parent='root')
        cur_folder = root
        for line in self.lines:
            if line == '$ cd ..':
                cur_folder = cur_folder.parent
            elif line.startswith('$ cd '):
                new_name = line.replace('$ cd ', '')
                if new_name not in cur_folder.children_names:
                    new_folder = Folder(name=new_name, parent=cur_folder)
                    all_folders.append(new_folder)
                    cur_folder.add_child(new_folder)
                    cur_folder = new_folder
                else:
                    cur_folder = cur_folder.child_by_key(new_name)
            elif line.startswith('dir '):
                name = line.replace('dir ', '')
                if name not in all_folders:
                    new = Folder(name=name, parent=cur_folder)
                    cur_folder.add_child(new)
                    all_folders.append(new)
            elif line == '$ ls':
                continue
            else:
                size = Parser.find_int_in(line)
                cur_folder.add_size(size)
            # print(line, cur_folder)
        # print(all_folders)
        total_size = root.size_of_children()
        max_allowed_size = 70000000 - 30000000
        size_needed = total_size - max_allowed_size
        poss = []
        for d in all_folders:
            if (x := d.size_of_children()) >= size_needed:
                poss.append(x)
        return min(poss)


if __name__ == '__main__':
    print(Solver().run())
