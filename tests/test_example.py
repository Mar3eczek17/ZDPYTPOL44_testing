import unittest


from account import Account

class ExampleTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(2 + 2, 4)

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(2 + 2, 5)

    @unittest.skip("Here goes reason why we skip this test")
    def test_01(self):
        self.assertEqual(2, 2)

    @unittest.skipIf(2 == 2, "Reason why we skip it")
    def test_02(self):
        self.assertEqual(2, 2)

    @unittest.skipUnless(2 == 2, "Reason why we skip it")
    def test_03(self):
        self.assertEqual(2, 2)

    def test_success(self):
        with self.assertRaises(ValueError):
            int("XXXX")

    def test_fail(self):
        with self.assertRaises(ValueError):
            int("1")

    def test_validate_name_raises_error_when_improper_value_given(self):
        with self.assertRaises(TypeError):
            Account(balance=100, name = 123, last_name = "last_name")

    def test_validate_name_raises_error_with_correct_messege(self):
        with self.assertRaisesRegex(TypeError, "Nsh"):
            Account(balance=100, name = 123, last_name = "last_name")


