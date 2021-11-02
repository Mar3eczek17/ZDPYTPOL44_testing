class Number:

    def __init__(self, value: int) -> None:
        self.value = value

    def __add__(self, other: "Number"):
        print("JEST WYWOŁANA!!!111")
        print(self.value + other.value)
        return self.value + other.value

    def __len__(self):
        print("WYWOŁAŁEM LENA")
        return 100

x = Number(4)
y = Number(5)
z = len(x)
print(z)
x + y