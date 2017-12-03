import csv
import day2
import unittest

class Day2Test(unittest.TestCase):
    def test1(self):
        spreadsheet = read_file("aoc/aoc-2017/data/day2_1_example.csv")
        self.assertEqual(day2.day2_1(spreadsheet), 18)
    def test2(self):
        spreadsheet = read_file("aoc/aoc-2017/data/day2_2_example.csv")
        self.assertEqual(day2.day2_2(spreadsheet), 9)

def read_file(filename):
    contents = []
    with open(filename) as file:
        reader = csv.reader(file, delimiter='\t')
        for line in reader:
            contents.append(map(int, line))
    return contents

if __name__ == '__main__':
    unittest.main()
