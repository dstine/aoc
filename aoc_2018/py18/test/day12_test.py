import py18.test.test_utils as test_utils
import py18.day12 as day12
import pytest

def test_part1():
    initial_state, rules = get_example_input()
    assert day12.part1(initial_state, rules, 20) == 325
    initial_state, rules = get_my_input()
    assert day12.part1(initial_state, rules, 20) == 2049

def test_part2():
    initial_state, rules = get_example_input()
    assert day12.part2_example(initial_state, rules, 20) == 325
    assert day12.part2_example(initial_state, rules, 100) == 1374
    initial_state, rules = get_my_input()
    assert day12.part2_input(initial_state, rules, 200) == 9206
    assert day12.part2_input(initial_state, rules, 50000000000) == 2300000000006

def get_my_input():
    path = test_utils.get_path('day12_input.txt')
    return get_input(path)

def get_example_input():
    path = test_utils.get_path('day12_example.txt')
    return get_input(path)

def get_input(path):
    initial_state = ''
    rules = {}
    with open(path) as file:
        for line in file.readlines():
            line = line.rstrip()
            if line.startswith('initial state: '):
                initial_state = line.split('initial state: ')[1]
            elif line:
                pattern, result = line.split(' => ')
                rules[pattern] = result
    return initial_state, rules

