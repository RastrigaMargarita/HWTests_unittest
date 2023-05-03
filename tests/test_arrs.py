import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([1, 2, 3], -1, None), None)
        self.assertEqual(arrs.get([1, 2, 3], -1553, "test"), "test")


    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -1, None), [3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -112, 2), [1, 2])
        self.assertEqual(arrs.my_slice([], 0, 2), [])

