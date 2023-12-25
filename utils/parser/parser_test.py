from utils.parser.parser import Parser


def test_split_into_equal_segments():
    s = "catbathat"
    assert Parser.split_into_equal_segments(s, 3) == ["cat", "bat", "hat"]


def test_remove_many():
    s = '[cat]'
    assert Parser.remove_many(s, '[]') == 'cat'


def test_split_twice():
    s = 'cat, bat: 3'
    assert Parser.split_twice_key(s, ":", ",") == (['cat', 'bat'], "3")
    s = 'cat, bat: 3; 4'
    assert Parser.split_twice_both(s, ":", ",", ";") == (['cat', 'bat'], ["3", "4"])
    s = 'cat: 3; 4'
    assert Parser.split_twice_val(s, ':', ';') == ("cat", ["3", "4"])


def test_find_int():
    # s = '34wefksjdf'
    # assert Parser.find_int_in(s) == 34
    s = 'skf sdfklj sdf 34123134'
    assert Parser.find_int_in(s) == 34123134