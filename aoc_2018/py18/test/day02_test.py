import py18.test.test_utils as test_utils
import py18.day02 as day02
import pytest

def test_count():
    assert day02.count('abcdef') == (False, False)
    assert day02.count('bababc') == (True, True)
    assert day02.count('abbcde') == (True, False)
    assert day02.count('abcccd') == (False, True)

def test_1():
    assert day02.part1(['abcdef', 'bababc', 'abbcde','abcccd', 'aabcdd', 'abcdee', 'ababab']) == 12
    my_input = get_my_input()
    assert day02.part1(my_input) == 6150

def test_compare():
    assert day02.compare('abcde', 'axcye') == (2, 'ace')
    assert day02.compare('fghij', 'fguij') == (1, 'fgij')

def test_2():
    assert day02.part2(['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']) == 'fgij'
    my_input = get_my_input()
    assert day02.part2(my_input) == 'rteotyxzbodglnpkudawhijsc'

def get_my_input():
    path = test_utils.get_path('day02_input.txt')
    with open(path) as file:
        return [line.rstrip() for line in file]
