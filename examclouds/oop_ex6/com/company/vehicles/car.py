from oop.examclouds.oop_ex6.com.company.professions.driver import Driver
from oop.examclouds.oop_ex6.com.company.details.engine import Engine

class Car:
    def __init__(self, marka: str, car_class: str, weight: float, driver: Driver, engine: Engine) -> None:
        self.marka = marka
        self.car_class = car_class
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def start(self):
        print("Поехали")

    def stop(self):
        print("Останавливаемся")

    def turn_right(self):
        print("Поворот направо")

    def turn_left(self):
        print("Поворот налево")

    def to_string(self):
        print(f"Автомобиль: {self.marka}"
              f"Класс автомобиля: {self.car_class}"
              f"Вес автомобиля: {self.weight}"
              f"Водитель: {self.driver}"
              f"Двигатель: {self.engine}")

class Lorry(Car):
    def __init__(self, marka: str, car_class: str, weight: float, driver: Driver, engine: Engine, carrying: float):
        super().__init__(marka, car_class, weight, driver, engine)
        self.carrying = carrying

class SportCar(Car):
    def __init__(self, marka: str, car_class: str, weight: float, driver: Driver, engine: Engine, speed: float):
        super().__init__(marka, car_class, weight, driver, engine)
        self.speed = speed