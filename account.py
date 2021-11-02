from random import choice
from typing import Optional
class Account:
    def __init__(self, balance: float, name: str, last_name: str, stock: str) -> None:
        self.balance = balance
        self.name = self.validate_name(name)
        self.last_name = last_name
        self.stock = stock
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
    def get_recommendation_from_external_api(self) -> Optional[str]:
        recommendation = external_api_recommendation()
        print(f"Current recommendation: {recommendation}")
        if recommendation[0] == self.stock:
            return self.buy()
    def buy(self) -> str:
        print(f"{self.stock} has been bought!")
        return self.stock
def external_api_recommendation():
    """
    Funkcja ma imitować zewnętrzny serwis www do rekomendacji ofert na giełdzie
    """
    responses = [
        ("APL", 123),
        ("FB", 12),
        ("GER", 456),
        ("RTY", 345),
        ("QWE", 890),
    ]
    return choice(responses)
# adam = Account(balance=123, name="Adam", last_name="Driver", stock="FB")
# for _ in range(50):
#     adam.get_recommendation_from_external_api()
