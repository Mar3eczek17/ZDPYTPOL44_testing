class Account:
    def __init__(self, balance: float, name: str) -> None:
        self.balance = balance
        self.name = name


    def transfer(self, amount: float) -> None:
        self.balance += amount


    def get_balance(self) -> float:
        return self.balance