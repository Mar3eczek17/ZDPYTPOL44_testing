import unittest


def setUpModule():
    print("I'm setUpModule!")


def tearDownModule():
    print("I'm tearDownModule!")


class SetUpTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("I'm setUpClass!")


    @classmethod
    def tearDownClass(cls) -> None:
        print("I'm tearDownClass!")


    def setUp(self) -> None:
        print("I'm setUp!")


    def tearDown(self) -> None:
        print("I'm tearDown!")


    def test_1(self):
        print("test_1")


    def test_2(self):
        print("test_2")


class SecondSetUpTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("I'm second setUpClass!")
    @classmethod
    def tearDownClass(cls) -> None:
        print("I'm second tearDownClass!")


    def setUp(self) -> None:
        print("I'm second setUp!")


    def tearDown(self) -> None:
        print("I'm second tearDown!")


    def test_1(self):
        print("second test_1")


    def test_2(self):
        print("second test_2")