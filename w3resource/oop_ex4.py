from math import pi


class Figure:
    @property
    def perimeter(self):
        pass

    @property
    def area(self):
        pass


class Circle(Figure):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    @property
    def perimeter(self) -> float:
        return round(2 * pi * self.radius)

    @property
    def area(self) -> float:
        return round(pi * self.radius**2)


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float, h: float) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    @property
    def perimeter(self) -> float:
        return round(self.a + self.b + self.c)

    @property
    def area(self) -> float:
        return round((self.a * self.h) / 2)


class Square(Figure):
    def __init__(self, a: float) -> None:
        self.a = a

    @property
    def perimeter(self) -> float:
        return round(4 * self.a)

    @property
    def area(self) -> float:
        return round(self.a**2)


trg = Triangle(1, 2, 6, 4)
print(trg.perimeter)
print(trg.area)
