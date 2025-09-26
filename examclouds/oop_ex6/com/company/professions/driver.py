from oop.examclouds.oop_ex6.com.company.professions.person import Person


class Driver(Person):
    def __init__(
        self, first_name: str, last_name: str, age: int, experience: int
    ) -> None:
        super().__init__(first_name, last_name, age)
        self.experience = experience
