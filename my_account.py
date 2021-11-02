class Account:
    def __init__(self, balance: float, name: str, last_name: str):
        self.balance = balance
        self.name = name
        self.last_name = last_name


    def get_owner(self) -> str:
        return f"{self.name} {self.last_name}"

    def get_balance(self) -> float:
        if self.balance < 0:
            print("You dont have enough founds!!!")
            return False
        else:
            return self.balance

    def deposit(self, amount: float) -> None:
        self.balance += amount
        if amount == 0:
            print("You can't deposit 0$.")
        elif amount < 0:
            print("You can't deposit negative numbers!")

    def withdraw(self, amount: float) -> float:
        self.balance -= amount
        if amount == 0:
            print("You can't withdraw 0$.")



    def correct_name_type(self):
        return type(self.name)

    def correct_last_name_type(self):
        return type(self.last_name)

    def correct_number_type(self):
        return type(self.balance)

#1. zrobic test i funkcje zeby nie mozna było wybrać wiecej niz jest na koncie balance
#2. upewnić sie i zrobic test ze podcza działania programu przekazywane argumenty sa poprawne
#3. uepnic sie i zrobic test ze dla withdraw i deposit liczby maja wlasciwe znaki
#4. upewnic sie i zrobic test ze nie mozemy deposit i withdraw O