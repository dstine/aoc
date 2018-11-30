import aoc_2017.test.test_utils as test_utils
import aoc_2017.day09 as day09
import pytest

def test_day9_1():
    assert day09.day9_1("{{{}}}") == 6
    assert day09.day9_1("{{},{}}") == 5
    assert day09.day9_1("{{{},{},{{}}}}") == 16
    assert day09.day9_1("{<a>,<a>,<a>,<a>}") == 1
    assert day09.day9_1("{{<ab>},{<ab>},{<ab>},{<ab>}}") == 9
    assert day09.day9_1("{{<!!>},{<!!>},{<!!>},{<!!>}}") == 9
    assert day09.day9_1("{{<a!>},{<a!>},{<a!>},{<ab>}}") == 3
    assert day09.day9_1(MY_INPUT) == 17537

def test_day9_2():
    assert day09.day9_2("<>") == 0
    assert day09.day9_2("<random characters>") == 17
    assert day09.day9_2("<<<<>") == 3
    assert day09.day9_2("<{!>}>") == 2
    assert day09.day9_2("<!!>") == 0
    assert day09.day9_2("<!!!>>") == 0
    assert day09.day9_2('<{o"i!a,<{i<a>') == 10
    assert day09.day9_2(MY_INPUT) == 7539

def readfile(filename):
    with open(filename) as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]

MY_INPUT = readfile(test_utils.get_path('day9_real.txt'))[0]
