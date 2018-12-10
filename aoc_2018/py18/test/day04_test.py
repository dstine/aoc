import py18.test.test_utils as test_utils
import py18.day04 as day04
import pytest

def test_part1():
    records = get_input('day04_example.txt')
    assert day04.part1(records) == 240
    records = get_input('day04_input.txt')
    assert day04.part1(records) == 118599

def test_part2():
    records = get_input('day04_example.txt')
    assert day04.part2(records) == 4455
    records = get_input('day04_input.txt')
    assert day04.part2(records) == 33949

def test_analyze_records():
    records = sorted(get_input('day04_example.txt'))
    expected = {
        10: {5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 2, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1, 42: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1, 49: 1, 50: 1, 51: 1, 52: 1, 53: 1, 54: 1, 25: 1, 26: 1, 27: 1, 28: 1},
        99: {40: 2, 41: 2, 42: 2, 43: 2, 44: 2, 45: 3, 46: 2, 47: 2, 48: 2, 49: 2, 36: 1, 37: 1, 38: 1, 39: 1, 50: 1, 51: 1, 52: 1, 53: 1, 54: 1},
    }
    assert day04.analyze_records(records) == expected

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
