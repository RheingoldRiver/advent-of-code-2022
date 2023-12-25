import re


class Parser:
    @staticmethod
    def split_into_equal_segments(s: str, num_chars: int):
        if num_chars > len(s):
            raise ValueError(f"num_chars is too big! String length is {len(s)}")
        return [s[i:i + num_chars] for i in range(0, len(s), num_chars)]

    @staticmethod
    def remove_many(s, chars_to_replace):
        for char in chars_to_replace:
            s = s.replace(char, '')
        return s

    @staticmethod
    def split_twice_key(s, outer_split, key_split):
        key, val = s.split(outer_split)
        return [x.strip() for x in key.split(key_split)], val.strip()

    @staticmethod
    def split_twice_val(s, outer_split, val_split):
        key, val = s.split(outer_split)
        return key.strip(), [x.strip() for x in val.strip().split(val_split)]

    @staticmethod
    def split_twice_both(s, outer_split, key_split, val_split):
        key, val = s.split(outer_split)
        return [x.strip() for x in key.split(key_split)], [x.strip() for x in val.split(val_split)]

    @staticmethod
    def lines(s):
        return s.split('\n')

    @staticmethod
    def find_int_in(s):
        match = re.search(r'(\d+)', s)
        try:
            return int(match[1])
        except TypeError:
            raise ValueError(f"cannot find number in {s}")
