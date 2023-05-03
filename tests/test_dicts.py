import unittest

from utils import dicts

class TestDict(unittest.TestCase):

    def test_val(self):
        self.assertEqual(dicts.get_val({1: "1", 2: "2", 3: "3"}, 1), "1")
        self.assertEqual(dicts.get_val({1: "1", 2: "2", 3: "3"}, None), "git")
        self.assertEqual(dicts.get_val({}, 1553), "git")
