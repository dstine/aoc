import aoc_2017.test.test_utils as test_utils
import aoc_2017.day16 as day16
import pytest

def test_day16_1():
    assert day16.day16_1('abcde', test_utils.get_path('day16_example.txt')) == 'baedc'
    assert day16.day16_1('abcdefghijklmnop', test_utils.get_path('day16_real.txt')) == 'hmefajngplkidocb'
