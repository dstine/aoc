import aoc_2017.day14 as day14
import pytest

def test_day14_1():
    assert day14.day14_1('flqrgnkx') == 8108
    assert day14.day14_1(MY_INPUT) == 8074

MY_INPUT = 'jzgqcdpd'
