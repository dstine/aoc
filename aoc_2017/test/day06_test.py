import aoc_2017.day06 as day06
import pytest

MY_INPUT = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]

def test_day6_1():
    assert day06.day6_1([0, 2, 7, 0]) == 5
    assert day06.day6_1(MY_INPUT) == 6681

def test_day6_2():
    assert day06.day6_2([0, 2, 7, 0]) == 4
    assert day06.day6_2(MY_INPUT) == 2392
