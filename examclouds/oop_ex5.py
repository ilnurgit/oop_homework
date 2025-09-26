class Student:

    def __init__(self, first_name: str, last_name: str, group: str, average_mark: float) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.average_mark = average_mark

    def get_scholarship(self) -> int:
        if self.average_mark == 5:
            return 2000
        elif 4 <= self.average_mark < 5:
            return 1900
        else:
            return 0


class Aspirant(Student):

    def get_scholarship(self) -> int:
        if self.average_mark == 5:
            return 2500
        elif 4 <= self.average_mark < 5:
            return 2200
        else:
            return 0


student1 = Student("Ivan", "Ivanov", "B", 4.5)
student2 = Student("Bob", "Magamedov", "C", 5)
student3 = Student("Diana", "Petrova", "F", 3.2)

aspirant1 = Aspirant("John", "Magamedov", "B", 4.5)
aspirant2 = Aspirant("Fedor", "Petrov", "C", 5)
aspirant3 = Aspirant("Varvara", "Ivanova", "F", 3.2)

students: list[Student] = [student1, student2, student3, aspirant1, aspirant2, aspirant3]
for student in students:
    print(f"{student.first_name} {student.last_name} получает степендию: {student.get_scholarship()} грн")
