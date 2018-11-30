import aoc_2017.test.test_utils as test_utils
import aoc_2017.day12 as day12
import pytest

def test_day12_1():
    assert day12.day12_1(test_utils.get_path('day12_example.txt')) == 6
    assert day12.day12_1(MY_INPUT) == 288

def test_day12_2():
    assert day12.day12_2(test_utils.get_path('day12_example.txt')) == 2
    assert day12.day12_2(MY_INPUT) == 211

MY_INPUT = test_utils.get_path('day12_real.txt')
