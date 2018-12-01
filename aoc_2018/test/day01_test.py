import aoc_2018.test.test_utils as test_utils
import aoc_2018.day01 as day01
import pytest

def test_1():
    assert day01.part1(['+1', '-2', '+3', '+1']) == 3
    assert day01.part1(['+1', '+1', '+1']) == 3
    assert day01.part1(['+1', '+1', '-2']) == 0
    assert day01.part1(['-1', '-2', '-3']) == -6
    my_input = get_my_input()
    assert day01.part1(my_input) == 400

def test_2():
    assert day01.part2(['+1', '-2', '+3', '+1']) == 2
    assert day01.part2(['+1', '-1']) == 0
    assert day01.part2(['+3', '+3', '+4', '-2', '-4']) == 10
    assert day01.part2(['-6', '+3', '+8', '+5', '-6']) == 5
    assert day01.part2(['+7', '+7', '-2', '-7', '-4']) == 14
    my_input = get_my_input()
    assert day01.part2(my_input) == 232

def get_my_input():
    path = test_utils.get_path('day01_input.txt')
    with open(path) as file:
        return [line for line in file]
