import aoc_2017.test.test_utils as test_utils
import aoc_2017.day07 as day07
import pytest

def test_parse_program():
    program = "ktlj (57)"
    result = {'name': 'ktlj',
             'weight': 57,
             'supported_names': [],
             'supported_weight': 0,
             'total_weight': 0}
    assert day07.parse_program(program) == result

    program = "fwft (72) -> ktlj, cntj, xhth"
    result = {'name': 'fwft',
             'weight': 72,
             'supported_names': ['ktlj', 'cntj', 'xhth'],
             'supported_weight': 0,
             'total_weight': 0}
    assert day07.parse_program(program) == result

def test_day7_1():
    assert day07.day7_1(EXAMPLE) == 'tknk'
    assert day07.day7_1(MY_INPUT) == 'hlqnsbe'

def test_day7_2():
    example = readfile(test_utils.get_path('day7_example.txt'))
    assert day07.day7_2(EXAMPLE) == 60
    assert day07.day7_2(MY_INPUT) == 1993

def readfile(filename):
    with open(filename) as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]

EXAMPLE = readfile(test_utils.get_path('day7_example.txt'))
MY_INPUT = readfile(test_utils.get_path('day7_real.txt'))
