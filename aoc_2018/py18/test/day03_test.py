import py18.test.test_utils as test_utils
import py18.day03 as day03
import pytest

def test_1():
    assert day03.part1(['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']) == 4
    assert day03.part1(get_my_input()) == 115304

def test_2():
    assert day03.part2(['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']) == 3
    assert day03.part2(get_my_input()) == 275

def test_parse_claim():
    assert day03.parse_claim('#1 @ 1,3: 4x4') == (1, 1, 3, 4, 4)
    assert day03.parse_claim('#2 @ 3,1: 4x4') == (2, 3, 1, 4, 4)
    assert day03.parse_claim('#3 @ 5,5: 2x2') == (3, 5, 5, 2, 2)
    assert day03.parse_claim('#1290 @ 325,121: 12x17') == (1290, 325, 121, 12, 17)

def test_assert_claim():
    fabric = day03.create_fabric(8, 8)
    expected = [
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
    ]
    assert fabric == expected

    claim1 = day03.parse_claim('#1 @ 1,3: 4x4')
    day03.assert_claim(fabric, claim1)
    expected = [
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 1, 1, 1, 1, 0, 0, 0, ],
        [0, 1, 1, 1, 1, 0, 0, 0, ],
        [0, 1, 1, 1, 1, 0, 0, 0, ],
        [0, 1, 1, 1, 1, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
    ]
    assert fabric == expected

    claim2 = day03.parse_claim('#2 @ 3,1: 4x4')
    day03.assert_claim(fabric, claim2)
    expected = [
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 1, 1, 1, 1, 0, ],
        [0, 0, 0, 1, 1, 1, 1, 0, ],
        [0, 1, 1, 2, 2, 1, 1, 0, ],
        [0, 1, 1, 2, 2, 1, 1, 0, ],
        [0, 1, 1, 1, 1, 0, 0, 0, ],
        [0, 1, 1, 1, 1, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
    ]
    assert fabric == expected

    claim3 = day03.parse_claim('#3 @ 5,5: 2x2')
    day03.assert_claim(fabric, claim3)
    expected = [
        [0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 1, 1, 1, 1, 0, ],
        [0, 0, 0, 1, 1, 1, 1, 0, ],
        [0, 1, 1, 2, 2, 1, 1, 0, ],
        [0, 1, 1, 2, 2, 1, 1, 0, ],
        [0, 1, 1, 1, 1, 1, 1, 0, ],
        [0, 1, 1, 1, 1, 1, 1, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, ],
    ]
    assert fabric == expected

def get_my_input():
    path = test_utils.get_path('day03_input.txt')
    with open(path) as file:
        return [line.rstrip() for line in file]
