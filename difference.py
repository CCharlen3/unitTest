import unittest

def find_difference(n1, n2):
    return n1 - n2

class TestFindDifference(unittest.TestCase):
    def test_positive_numbers(self):
        result = find_difference(10, 3)
        self.assertEqual(result, 7)

    def test_negative_numbers(self):
        result = find_difference(-21, -9)
        self.assertEqual(result, -12)

    def test_positive_and_negative_numbers(self):
        result = find_difference(18, -5)
        self.assertEqual(result, 23)

if __name__ == '__main__':
    unittest.main()
