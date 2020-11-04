import unittest
from example_pkg_komigabor.calculator import sub


class TestSub(unittest.TestCase):

    def test_sub(self):
        self.assertEqual(2, sub(5, 3), "Should be 2")
        self.assertEqual(17, sub(28, 11), "Should be 17")
        self.assertEqual(94, sub(157, 63), "Should be 94")

    def test_sub_negative(self):
        self.assertEqual(8, sub(3, -5), "Should be 8")
        self.assertEqual(-8, sub(-3, 5), "Should be -8")
        self.assertEqual(2, sub(-3, -5), "Should be 2")
