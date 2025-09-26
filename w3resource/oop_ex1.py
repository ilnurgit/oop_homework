from math import pi


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    @property
    def area(self) -> float:
        return round(pi * self.radius**2, 2)

    @property
    def perimetr(self) -> float:
        return round(2 * pi * self.radius, 2)


radius = float(input("Введите пожалуйста радиус круга: "))
circle1 = Circle(radius)
print("Площадь круга:", circle1.area, "см2")
print("Периметр круга:", circle1.perimetr, "см")
