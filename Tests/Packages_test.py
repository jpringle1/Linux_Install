import unittest
import pytest_cov 

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_positive_and_negative(self):
        self.assertEqual(add(1, -1), 0)

    def test_add_zeros(self):
        self.assertEqual(add(0, 0), 0)