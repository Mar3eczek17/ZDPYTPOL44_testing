import unittest
from unittest.mock import patch, MagicMock
from account import Account
class AccountTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.name = "John"
        self.last_name = "Doe"
        self.balance = 100
        self.name2 = "Woody"
        self.last_name2 = "Harrelson"
        self.balance2 = 1000
        self.account = Account(self.balance, self.name, self.last_name, "FB")
        self.account2 = Account(self.balance2, self.name2, self.last_name2, "FB")
    def test_get_owner_returns_full_name(self):
        expected_result = f"{self.name} {self.last_name}"
        self.assertEqual(self.account.get_owner(), expected_result)
    def test_get_balance_returns_current_balance(self):
        expected_result = self.balance
        self.assertEqual(self.account.get_balance(), expected_result)
    def test_deposit_adds_proper_amount_to_owner_balance(self):
        sum_to_deposit = 50
        expected_result = self.account.get_balance() + sum_to_deposit
        self.account.deposit(sum_to_deposit)
        self.assertEqual(self.account.get_balance(), expected_result)
    def test_withdraw_subtract_proper_amount_from_owner_account(self):
        sum_to_withdraw = 50
        expected_result = self.account.get_balance() - sum_to_withdraw
        self.account.withdraw(sum_to_withdraw)
        self.assertEqual(self.account.get_balance(), expected_result)
    def test_withdraw_return_message_when_withdrawal_amount_gt_balance(self):
        sum_to_withdraw = 1000
        expected_result = "Withdrawal amount cannot be greater than current balance"
        result = self.account.withdraw(sum_to_withdraw)
        self.assertEqual(result, expected_result)
        self.assertEqual(self.account.get_balance(), self.balance)
    def test_transfer_to_decrease_proper_amount_from_sender_accounts_balance(self):
        amount = 50
        expected_result = self.account.get_balance() - amount
        self.account.transfer_to(amount, self.account2)
        self.assertEqual(self.account.get_balance(), expected_result)
    def test_transfer_to_increased_proper_on_receiver_accounts_balance(self):
        amount = 50
        expected_result = self.account2.get_balance() + amount
        self.account.transfer_to(amount, self.account2)
        self.assertEqual(self.account2.get_balance(), expected_result)
    def test_validate_name_raises_error_when_improper_value_given(self):
        with self.assertRaises(TypeError):
            Account(balance=100, name=123, last_name="last_name", stock="FB")
    def test_validate_name_raises_error_with_correct_message(self):
        with self.assertRaisesRegex(TypeError, "Name must be string!"):
            Account(balance=100, name=123, last_name="last_name", stock="FB")
    @patch("account.external_api_recommendation", return_value=("FB", 12))
    def test_get_recommendation_from_external_api_when_should_buy(self, external_api_mock):
        self.account.buy = MagicMock()
        self.account.get_recommendation_from_external_api()
        self.account.buy.assert_called_once()
    def test_get_recommendation_from_external_api_when_shouldnt_buy(self):
        pass