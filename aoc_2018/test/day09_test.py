import aoc_2018.test.test_utils as test_utils
import aoc_2018.day09 as day09
import pytest

def test_part1():
    assert day09.part1(9, 25) == 32
    assert day09.part1(10, 1618) == 8317
    assert day09.part1(13, 7999) == 146373
    assert day09.part1(17, 1104) == 2764
    assert day09.part1(21, 6111) == 54718
    assert day09.part1(30, 5807) == 37305
    # my input
    assert day09.part1(476, 71657) == 386018
