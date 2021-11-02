import unittest

from account import Account

class AccountTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.name = "John"
        self.last_name = "Doe"
        self.balance = 100
        self.account = Account(self.balance,self.name, self.last_name)


    def test_get_owner_returns_full_name(self):
        expected_result = f"{self.name} {self.last_name}"


        self.assertEqual(self.account.get_owner(), expected_result)


    def test_get_balance_returns_current_balance(self):
        expected_result = self.balance

        self.assertEqual(self.account.get_balance(), expected_result)

    def test_deposit_adds_proper_account_to_owner_balance (self):
        sum_to_deposit = 50
        expected_result = self.account.get_balance() + sum_to_deposit

        self.account.deposit(sum_to_deposit)

        self.assertEqual(self.account.get_balance(), expected_result)

    def test_withdraw_substract_proper_amount_from_owner_account(self):
        sum_to_withdraw = 50
        expected_result = self.account.get_balance() - sum_to_withdraw


        self.account.withdraw(sum_to_withdraw)
        self.assertEqual(self.account.get_balance(), expected_result)

    def test_there_is_no_overwithdrawal(self):
        sum_to_withdraw = 10
        expected_result = self.account.get_balance() - sum_to_withdraw


        self.account.withdraw(sum_to_withdraw)
        self.assertEqual(self.account.get_balance(), expected_result)

    def test_if_entered_name_is_of_correct_type(self):
        self.name = type("Zosia")
        expected_result = self.account.correct_name_type()


        self.assertEqual(self.name, expected_result)


    def test_if_entered_last_name_is_of_correct_type(self):
            self.last_name = type("Smith")
            expected_result = self.account.correct_last_name_type()


            self.assertEqual(self.last_name, expected_result)

    def test_if_entered_numbers_are_correct(self):
        self.balance = type(50)
        expected_result = self.account.correct_number_type()


        self.assertEqual(self.balance, expected_result)

    def test_if_deposit_in_not_zero(self):
        sum_to_deposit = 0
        expected_result = self.account.get_balance() + sum_to_deposit

        self.account.deposit(sum_to_deposit)

        self.assertNotEqual(self.balance, expected_result)

    def test_if_withdraw_in_not_zero(self):
        sum_to_withdraw = 0
        expected_result = self.account.get_balance() + sum_to_withdraw

        self.account.withdraw(sum_to_withdraw)

        self.assertNotEqual(self.balance, expected_result)















