import unittest
from example_pkg_komigabor.calculator import add


class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(8, add(3, 5), "Should be 8")
        self.assertEqual(39, add(11, 28), "Should be 39")
        self.assertEqual(220, add(157, 63), "Should be 220")

    def test_add_negative(self):
        self.assertEqual(-2, add(3, -5), "Should be -2")
        self.assertEqual(2, add(-3, 5), "Should be 2")
        self.assertEqual(-8, add(-3, -5), "Should be -8")
