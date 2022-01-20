# Создать класс, описывающий группу студентов - `Group`.
#
# Данный класс хранит студентов в виде списка объектов `Student` также
# реализованного в виде соответствующего класса.
#
# В классах `Group` и `Student` реализовать необходимый набор атрибутов.
#
# Где класс `Student` минимум должен иметь атрибуты `name`, `age`, `grades`
#
# Реализовать необходимый набор методов экземпляра для работы с этими
# экземплярами:
# Класс `Group` умеет выводить на печать имена и оценки студентов.
# Наследование здесь не понадобится.


class Group:

    def __init__(self):
        self.students = []

    # Метод добавляет нового студента, по имени, возрасту и его оценке
    def add_student(self, name, age, grade):
        self.students.append(Student(name, age, grade))

    # Метод выводящий на печать имена и оценки студентов
    def get_group_info(self):
        for i in self.students:
            i.get_student_grades()

    # Метод для удаления студента(последнего добавленного если без
    # параметров) или конкретного студента в списке students
    def remove_student(self, id):
        try:
            self.students.pop(id)

        except Exception:
            print('id is not found, please check id')

    # Метод возвращает ссылку на конкретного студента по его номеру в списке
    def get_student(self, id):
        try:
            return self.students[id]

        except Exception:
            print('id is not found, please check id')


class Student:

    def __init__(self, name, age, grade):
        self.set_name(name)
        self.set_age(age)
        self.set_grade(grade)

    def set_name(self, setname=''):
        try:
            self.name = setname
        except Exception:

            print('Incorrect name, please check name!')

    def set_age(self, setage):
        self.age = setage

    def set_grade(self, setgrade):
        self.grades = setgrade

    def get_student(self):
        return self.name, self.age, self.grades

    def get_student_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def get_student_grades(self):
        print(self.name, self.grades, sep='\t')


group1 = Group()
group1.add_student('Alex', 29, 1447)
group1.add_student('Dimas', 29, 2000)
group1.add_student('Vasili', 33, 2150)
group1.add_student('Roman', 44, 1000)
group1.add_student('Fedor', 24, 1150)
group1.add_student('Konstantin', 21, 1478)
group1.remove_student(3)
group1.get_group_info()