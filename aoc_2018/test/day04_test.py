import aoc_2018.test.test_utils as test_utils
import aoc_2018.day04 as day04
import pytest

def test_part1():
    records = get_input('day04_example.txt')
    assert day04.part1(records) == 240
    records = get_input('day04_input.txt')
    assert day04.part1(records) == 118599

def test_parse_records():
    records = sorted(get_input('day04_example.txt'))
    expected = [
        (10, 5, 25),
        (10, 30, 55),
        (99, 40, 50),
        (10, 24, 29),
        (99, 36, 46),
        (99, 45, 55)
    ]
    assert day04.parse_records(records) == expected

def get_input(filename):
    path = test_utils.get_path(filename)
    with open(path) as file:
        return [line.rstrip() for line in file]

def get_my_input():
    path = test_utils.get_path('day04_input.txt')
    with open(path) as file:
        return [line.rstrip() for line in file]
