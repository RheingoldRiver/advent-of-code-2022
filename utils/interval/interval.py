from copy import deepcopy
from typing import Callable


class Interval:
    is_empty = False

    def __init__(self, min_value: int, max_value: int):
        self.min = min_value
        self.max = max_value

    @property
    def size(self):
        return self.max - self.min

    @classmethod
    def from_range(cls, min_value, max_value):
        return cls(min_value, max_value)

    @classmethod
    def from_min_and_size(cls, min_value, interval_size):
        return cls(min_value, interval_size + min_value)

    def __iter__(self):
        for i in range(self.min, self.max + 1):
            yield i

    def intersection_with(self, other: "Interval") -> "Interval":
        if self.min > other.max:
            # {  } [  ] --> x
            return EmptyInterval()
        if self.max < other.min:
            # [  ] {  } --> x
            return EmptyInterval()
        if self.min <= other.min and self.max >= other.max:
            # [  {  }  ] --> {  }
            return deepcopy(other)
        if self.min > other.min and self.max < other.max:
            # {  [  ]  } --> [  ]
            return deepcopy(self)
        if other.max >= self.min >= other.min:
            # {  [  }  ] --> [  }
            return Interval(self.min, other.max)
        if self.max >= other.min >= self.min:
            # [  {  ]  } --> {  ]
            return Interval(other.min, self.max)

    def subtract_other(self, other: "Interval") -> "MultiInterval":
        if self.min > other.max:
            # {  } [  ] --> [  ]
            return MultiInterval(deepcopy(self))
        if self.max < other.min:
            # [  ] {  } --> [  ]
            return MultiInterval(deepcopy(self))
        if self.min < other.min and self.max > other.max:
            # [  {  }  ] --> [ {  and } ]
            return MultiInterval(Interval(self.min, other.min - 1), Interval(other.max + 1, self.max))
        if self.min >= other.min and self.max <= other.max:
            # {  [  ]  } --> x
            return MultiInterval(EmptyInterval())
        if self.max > other.max >= self.min:
            # {  [  }  ] --> }  ]
            return MultiInterval(Interval(other.max + 1, self.max))
        if self.max >= other.min > self.min:
            # [  {  ]  } --> [  {
            return MultiInterval(Interval(self.min, other.min - 1))

    def union_with(self, other: "Interval") -> "MultiInterval":
        if self.min > other.max:
            # {  } [  ]
            return MultiInterval(deepcopy(self), deepcopy(other))
        if self.max < other.min:
            # [  ] {  }
            return MultiInterval(deepcopy(self), deepcopy(other))
        if self.min <= other.min and self.max >= other.max:
            # [  {  }  ]
            return MultiInterval(deepcopy(self))
        if self.min > other.min and self.max < other.max:
            # {  [  ]  }
            return MultiInterval(deepcopy(other))
        if other.max >= self.min >= other.min:
            # {  [  }  ]
            return MultiInterval(Interval(other.min, self.max))
        if self.max >= other.min >= self.min:
            # [  {  ]  }
            return MultiInterval(Interval(self.min, other.max))

    def transform(self, f: Callable[[int], int]) -> None:
        new_min = f(self.min)
        new_max = f(self.max)
        self.min = new_min if new_min < new_max else new_max
        self.max = new_max if new_min < new_max else new_min


class EmptyInterval(Interval):
    is_empty = True

    def __init__(self):
        super().__init__(0, 0)

    @property
    def size(self):
        return 0


class MultiInterval:
    def __init__(self, *intervals: Interval):
        self.intervals = intervals

    @property
    def is_empty(self):
        return self.num_segments == 0 or all([i.is_empty for i in self.intervals])

    @property
    def min(self) -> int:
        return min([i.min for i in self.intervals])

    @property
    def max(self) -> int:
        return max([i.max for i in self.intervals])

    @property
    def num_segments(self) -> int:
        return len(self.intervals)
