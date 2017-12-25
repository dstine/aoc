import test.test_utils as test_utils
import day05
import csv
import unittest

class Day05Test(unittest.TestCase):

    def test_day5_1(self):
        self.assertEqual(day05.day5_1([0, 3,  0,  1,  -3]), 5)
        self.assertEqual(day05.day5_1(list(MY_INPUT)), 372671)

    def test_day5_2(self):
        self.assertEqual(day05.day5_2([0, 3,  0,  1,  -3]), 10)
        self.assertEqual(day05.day5_2(list(MY_INPUT)), 25608480)

def read_file(filename):
    with open(filename) as file:
        content = file.readlines()
        content = [int(val.replace("\n", "")) for val in content]
        return content

MY_INPUT = read_file(test_utils.get_path("day5_real.csv"))

if __name__ == '__main__':
    unittest.main()
