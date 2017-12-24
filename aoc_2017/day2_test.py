import csv
import day2
import test_utils
import unittest

class Day2Test(unittest.TestCase):
    def test1(self):
        example = read_file(test_utils.get_path(__file__, "day2_1_example.csv"))
        self.assertEqual(day2.day2_1(example), 18)
        self.assertEqual(day2.day2_1(MY_INPUT), 51139)
    def test2(self):
        example = read_file(test_utils.get_path(__file__, "day2_2_example.csv"))
        self.assertEqual(day2.day2_2(example), 9)
        self.assertEqual(day2.day2_2(MY_INPUT), 272)

def read_file(filename):
    with open(filename) as file:
        reader = csv.reader(file, delimiter='\t')
        return [[int(field) for field in line] for line in reader]

MY_INPUT = read_file(test_utils.get_path(__file__, "day2_real.csv"))

if __name__ == '__main__':
    unittest.main()
