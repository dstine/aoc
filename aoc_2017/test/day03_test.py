import aoc_2017.day03 as day03
import pytest

MY_INPUT = 368078

def test_1():
    assert day03.day3_1(1) == 0
    assert day03.day3_1(2) == 1
    assert day03.day3_1(3) == 2
    assert day03.day3_1(9) == 2
    assert day03.day3_1(10) == 3
    assert day03.day3_1(12) == 3
    assert day03.day3_1(23) == 2
    assert day03.day3_1(1024) == 31
    assert day03.day3_1(MY_INPUT) == 371

def test_2():
    assert day03.day3_2(30) == 54
    assert day03.day3_2(MY_INPUT) == 369601
