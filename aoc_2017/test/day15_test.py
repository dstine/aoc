import aoc_2017.day15 as day15
import pytest

def test_day15_1():
    num_pairs = 40000000
    assert day15.day15_1(65, 8921, num_pairs) == 588
    assert day15.day15_1(516, 190, num_pairs) == 597

def test_day15_2():
    num_pairs = 5000000
    assert day15.day15_2(65, 8921, num_pairs) == 309
    assert day15.day15_2(516, 190, num_pairs) == 303
