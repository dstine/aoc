import aoc_2017.test.test_utils as test_utils
import aoc_2017.day04 as day04
import pytest

MY_INPUT = test_utils.get_path("day4_real.csv")

def test_is_valid_phrase():
    assert day04.is_valid_phrase(["aa", "bb", "cc", "dd", "ee"], day04.equals_test) == True
    assert day04.is_valid_phrase(["aa", "bb", "cc", "dd", "aa"], day04.equals_test) == False

def test_day4_1():
    assert day04.day4_1(test_utils.get_path("day4_1_example.csv")) == 1
    assert day04.day4_1(MY_INPUT) == 383

def test_day4_2():
    assert day04.day4_2(test_utils.get_path("day4_2_example.csv")) == 3
    assert day04.day4_2(MY_INPUT) == 265
