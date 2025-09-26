from datetime import date, datetime


class Person:

    def __init__(self, name: str, country: str, date_of_birth: date) -> None:
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    @property
    def determine_age(self) -> int:
        today = date.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) > (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age


ilnur = Person(name="Ilnur", country="Russia", date_of_birth=date(1993, 4, 1))
print(ilnur.date_of_birth)
print(ilnur.determine_age)
