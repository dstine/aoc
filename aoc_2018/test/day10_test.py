import aoc_2018.test.test_utils as test_utils
import aoc_2018.day10 as day10
import pytest

def test_part1():
    assert day10.part1(get_example_input()) == get_example_result()
    assert day10.part1(get_my_input()) == get_my_result()

def get_my_input():
    path = test_utils.get_path('day10_input.txt')
    return get_input(path)

def get_example_input():
    path = test_utils.get_path('day10_example.txt')
    return get_input(path)

def get_input(path):
    with open(path) as file:
        return [line.rstrip() for line in file]

def get_my_result():
    path = test_utils.get_path('day10_result.txt')
    return get_result(path)

def get_example_result():
    path = test_utils.get_path('day10_example_result.txt')
    return get_result(path)

def get_result(path):
    s = ''
    with open(path) as file:
        for line in file:
            s += line
    return s
