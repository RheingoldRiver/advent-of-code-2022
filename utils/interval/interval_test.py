from utils.interval.interval import Interval


def test_intersection():
    interval = Interval(5, 10)
    new = interval.intersection_with(Interval(1, 6))
    assert (new.min, new.max) == (5, 6)
    new = interval.intersection_with(Interval(8, 13))
    assert (new.min, new.max) == (8, 10)
    new = interval.intersection_with(Interval(6, 7))
    assert (new.min, new.max) == (6, 7)
    new = interval.intersection_with(Interval(1, 20))
    assert (new.min, new.max) == (5, 10)
    new = interval.intersection_with(Interval(0, 3))
    assert new.is_empty is True
    new = interval.intersection_with(Interval(20, 30))
    assert new.is_empty is True


def test_union():
    interval = Interval(5, 10)
    new = interval.union_with(Interval(1, 6))
    assert (new.min, new.max) == (1, 10)
    new = interval.union_with(Interval(8, 13))
    assert (new.min, new.max) == (5, 13)
    new = interval.union_with(Interval(6, 7))
    assert (new.min, new.max) == (5, 10)
    new = interval.union_with(Interval(1, 20))
    assert (new.min, new.max) == (1, 20)
    new = interval.union_with(Interval(0, 3))
    assert (new.min, new.max) == (0, 10)
    assert new.num_segments == 2
    new = interval.union_with(Interval(20, 30))
    assert (new.min, new.max) == (5, 30)
    assert new.num_segments == 2


def test_subtract():
    interval = Interval(5, 10)
    new = interval.subtract_other(Interval(1, 6))
    assert (new.min, new.max) == (7, 10)
    new = interval.subtract_other(Interval(8, 13))
    assert (new.min, new.max) == (5, 7)
    new = interval.subtract_other(Interval(6, 7))
    assert (new.min, new.max) == (5, 10)
    assert new.num_segments == 2
    assert new.intervals[0].max == 5
    assert new.intervals[1].min == 8
    new = interval.subtract_other(Interval(1, 20))
    assert new.is_empty is True
    new = interval.subtract_other(Interval(0, 3))
    assert (new.min, new.max) == (5, 10)
    new = interval.subtract_other(Interval(20, 30))
    assert (new.min, new.max) == (5, 10)
