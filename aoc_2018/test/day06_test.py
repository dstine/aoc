import aoc_2018.test.test_utils as test_utils
import aoc_2018.day06 as day06
import pytest

example_coords = [
    (1, 1), 
    (1, 6), 
    (8, 3), 
    (3, 4), 
    (5, 5), 
    (8, 9),
]

def test_part1():
    assert day06.part1(example_coords) == 17
    assert day06.part1(get_my_input()) == 3647

def test_label_nearest():
    assert day06.label_nearest((0, 0), example_coords) == 0
    assert day06.label_nearest((3, 4), example_coords) == 3
    assert day06.label_nearest((2, 5), example_coords) == -1

def test_part2():
    assert day06.part2(example_coords, 32) == 16
    assert day06.part2(get_my_input(), 10000) == 41605

def test_label_total_distance():
    assert day06.label_total_distance((4, 3), example_coords) == 30

def test_distance():
    assert day06.distance((0, 0), (1, 1)) == 2
    assert day06.distance((6, 3), (1, 1)) == 7
    assert day06.distance((10, 3), (4, 5)) == 8

def get_my_input():
    path = test_utils.get_path('day06_input.txt')
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    coords = [(line.split(', ')) for line in lines]
    coords = [(int(c[0]), int(c[1])) for c in coords]
    return coords
