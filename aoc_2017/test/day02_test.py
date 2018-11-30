import aoc_2017.test.test_utils as test_utils
import aoc_2017.day02 as day02
import csv
import pytest

def test_1():
    example = read_file(test_utils.get_path("day2_1_example.csv"))
    assert day02.day2_1(example) == 18
    assert day02.day2_1(MY_INPUT) == 51139
def test_2():
    example = read_file(test_utils.get_path("day2_2_example.csv"))
    assert day02.day2_2(example) == 9
    assert day02.day2_2(MY_INPUT) == 272

def read_file(filename):
    with open(filename) as file:
        reader = csv.reader(file, delimiter='\t')
        return [[int(field) for field in line] for line in reader]

MY_INPUT = read_file(test_utils.get_path("day2_real.csv"))
