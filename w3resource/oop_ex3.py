class Calculator:

    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    @property
    def add(self) -> float:
        return self.a + self.b

    @property
    def substraction(self) -> float:
        return self.a - self.b

    @property
    def multiplication(self) -> float:
        return self.a * self.b

    @property
    def division(self) -> float:
        if self.b == 0:
            raise ZeroDivisionError("На ноль делить нельзя!")
        return self.a / self.b


a = Calculator(2, 1)
print(a.add)
print(a.substraction)
print(a.multiplication)
print(a.division)
