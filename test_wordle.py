import unittest
from main import check_guess  # If this function exists

class TestWordle(unittest.TestCase):
    def test_correct_guess(self):
        self.assertEqual(check_guess('apple', 'apple'), '[G][G][G][G][G]')

    def test_incorrect_guess(self):
        self.assertEqual(check_guess('apple', 'baker'), '[_][Y][_][_][_]')
