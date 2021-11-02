from typing import Optional


class Account:
    def __init__(self, balance: float, name: str, last_name: str) -> None:
        self.balance = balance
        self.name = self.validate_name(name)
        self.last_name = last_name

    def get_owner(self) -> str:
        return f"{self.name} {self.last_name}"

    def get_balance(self) -> float:
        return self.balance

    def deposit(self, amount: float) -> Optional[str]:
        amount_is_a_number = isinstance(amount, (float, int))
        if not amount_is_a_number or amount <= 0:
            return "Amount value must be number which is greater than zero!"
        self.balance += amount

    def withdraw(self, amount: float) -> Optional[str]:
        if self.balance < amount:
            return "Withdrawal amount cannot be greater than current balance"
        self.balance -= amount

    def validate_name(self, name: str) -> str:
        if not isinstance(name, str):
            raise TypeError("Name must be string!")
        return name

    def transfer_to(self, amount: float, account: "Account") -> None:
        self.withdraw(amount)
        account.deposit(amount)