import aoc_2018.test.test_utils as test_utils
import aoc_2018.day05 as day05
import pytest

def test_part1():
    assert day05.part1('aA') == 0
    assert day05.part1('abBA') == 0
    assert day05.part1('abAB') == 4
    assert day05.part1('aabAAB') == 6
    assert day05.part1('dabAcCaCBAcCcaDA') == 10
    assert day05.part1(get_my_input()) == 10888

def test_react():
    assert day05.react('aA') == ''
    assert day05.react('abBA') == ''
    assert day05.react('abAB') == 'abAB'
    assert day05.react('aabAAB') == 'aabAAB'
    assert day05.react('dabAcCaCBAcCcaDA') == 'dabCBAcaDA'
    # my test cases
    #assert day05.react('aaaA') == 'aa'
    assert day05.react('aaaAb') == 'aab'
    # my input
    assert day05.react(get_my_input()) == get_my_input_reacted()

def get_my_input():
    path = test_utils.get_path('day05_input.txt')
    return get_one_liner(path)

def get_my_input_reacted():
    path = test_utils.get_path('day05_input_reacted.txt')
    return get_one_liner(path)

def get_one_liner(path):
    with open(path) as file:
        # only one line in file
        for line in file:
            return line.rstrip()
