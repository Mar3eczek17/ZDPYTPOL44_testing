import unittest


from parameterized import parameterized


class TestSequence(unittest.TestCase):
    @parameterized.expand ([
        ["foo", "a", "a"],
        ["bar", "a", "b"],
        ["lee", "b", "b"],
    ])
    def test_sequence(self, name, a, b):
        self.assertEqual(a, b)
