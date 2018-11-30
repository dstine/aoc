import aoc_2017.test.test_utils as test_utils
import aoc_2017.day10 as day10
import pytest

def test_day10_1():
    assert day10.day10_1(5, '3,4,1,5') == 12
    assert day10.day10_1(256, MY_INPUT) == 6909

def test_as_ascii():
    assert day10.as_ascii('3,4,1,5') == [51, 44, 52, 44, 49, 44, 53]
    assert day10.as_ascii('1,2,3') == [49,44,50,44,51]

def test_bitwise_xor():
    assert day10.bitwise_xor([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]) == 64

def test_day10_2():
    assert day10.day10_2(256, '') == 'a2582a3a0e66e6e86e3812dcb672a272'
    assert day10.day10_2(256, 'AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
    assert day10.day10_2(256, '1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
    assert day10.day10_2(256, '1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'
    assert day10.day10_2(256, MY_INPUT) == '9d5f4561367d379cfbf04f8c471c0095'

def readfile(filename):
    with open(filename) as file:
        line = file.readline()
        return line

MY_INPUT = readfile(test_utils.get_path('day10_real.txt'))
