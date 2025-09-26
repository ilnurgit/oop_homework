from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def make_noise(self) -> str:
        ...

    @abstractmethod
    def eat(self) -> str:
        ...

    @abstractmethod
    def get_description(self) -> str:
        ...

class Dog(Animal):
    def make_noise(self) -> str:
        return "ГАВ - ГАВ"

    def eat(self) -> str:
        return "мясо"

    def get_description(self) -> str:
        return "злой"

class Cat(Animal):
    def make_noise(self) -> str:
        return "МЯУ - МЯУ"

    def eat(self) -> str:
        return "молоко"

    def get_description(self) -> str:
        return "добрый"

class Bear(Animal):
    def make_noise(self) -> str:
        return "РРР - РРР"

    def eat(self) -> str:
        return "мясо, мёд"

    def get_description(self) -> str:
        return "большой и злой"

class Vet:
    def treat_animal(self, animal: Animal) -> None:
        print(f"Пациент: {animal.name}")
        print(f"Описание пациента: {animal.get_description()}")

def main() -> None:
    vet = Vet()
    animals: list[Animal] = [
        Dog("Шарик"),
        Cat("Мурка"),
        Bear("Потапыч"),
    ]

    # цикл приема у ветеринара
    for animal in animals:
        vet.treat_animal(animal)
        print("-" * 20)

    # отдельный цикл: звуки и еда
    for animal in animals:
        print(f"{animal.name} издает звук: {animal.make_noise()}")
        print(f"{animal.name} питается: {animal.eat()}")
        print("-" * 20)

if __name__ == "__main__":
    main()