import py18.test.test_utils as test_utils
import py18.day11 as day11
import pytest

def test_part1():
    assert day11.part1(18) == (33, 45)
    assert day11.part1(42) == (21, 61)
    assert day11.part1(9995) == (33, 45)

def xtest_part2():
    assert day11.part2(18) == (90, 269, 16)
    assert day11.part2(42) == (232, 251, 12)
    assert day11.part2(9995) == (233, 116, 15)

def test_calc_power():
    assert day11.calc_power((3, 5), 8) == 4
    assert day11.calc_power((122, 79), 57) == -5
    assert day11.calc_power((217, 196), 39) == 0
    assert day11.calc_power((101, 153), 71) == 4
