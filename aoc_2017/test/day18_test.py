import aoc_2017.test.test_utils as test_utils
import aoc_2017.day18 as day18
import pytest

example_input = [
    'set a 1',
    'add a 2',
    'mul a a',
    'mod a 5',
    'snd a',
    'set a 0',
    'rcv a',
    'jgz a -1',
    'set a 1',
    'jgz a -2',
]

def test_part1():
    assert day18.part1(example_input) == 4
    assert day18.part1(get_my_input()) == 3188

def get_my_input():
    path = test_utils.get_path('day18_input.txt')
    with open(path) as file:
        return [line.rstrip() for line in file]
