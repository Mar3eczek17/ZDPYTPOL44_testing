import unittest


class StartTestCase(unittest.TestCase):
    def test_start(self):
        self.assertTrue(True)


    def test_fail(self):
        self.assertTrue(False)