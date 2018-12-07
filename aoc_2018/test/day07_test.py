import aoc_2018.test.test_utils as test_utils
import aoc_2018.day07 as day07
import pytest

example_input = [
    'Step C must be finished before step A can begin.',
    'Step C must be finished before step F can begin.',
    'Step A must be finished before step B can begin.',
    'Step A must be finished before step D can begin.',
    'Step B must be finished before step E can begin.',
    'Step D must be finished before step E can begin.',
    'Step F must be finished before step E can begin.',
]

def test_part1():
    assert day07.part1(example_input) == 'CABDFE'
    assert day07.part1(get_my_input()) == 'MNQKRSFWGXPZJCOTVYEBLAHIUD'

def test_parse():
    assert day07.parse(example_input) == [
        ('C', 'A'),
        ('C', 'F'),
        ('A', 'B'),
        ('A', 'D'),
        ('B', 'E'),
        ('D', 'E'),
        ('F', 'E'),
    ]

def get_my_input():
    path = test_utils.get_path('day07_input.txt')
    with open(path) as file:
        return [line.rstrip() for line in file]
