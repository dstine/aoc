import aoc_2018.test.test_utils as test_utils
import aoc_2018.day08 as day08
import pytest

example_input = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

def test_part1():
    assert day08.part1(example_input) == 138
    assert day08.part1(get_my_input()) == 45194

def test_part2():
    assert day08.part2(example_input) == 66
    assert day08.part2(get_my_input()) == 22989

def get_my_input():
    path = test_utils.get_path('day08_input.txt')
    with open(path) as file:
        # only one line in file
        for line in file:
            numbers = line.rstrip().split(' ')
    return [int(n) for n in numbers]
