import aoc_2017.test.test_utils as test_utils
import aoc_2017.day13 as day13
import pytest

def test_day13_1():
    assert day13.day13_1(test_utils.get_path('day13_example.txt')) == 24
    assert day13.day13_1(MY_INPUT) == 1316

def test_day13_2():
    assert day13.day13_2(test_utils.get_path('day13_example.txt')) == 10
    assert day13.day13_2(MY_INPUT) == 3840052

MY_INPUT = test_utils.get_path('day13_real.txt')
