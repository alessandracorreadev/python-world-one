class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def happy_bday(self):
        self.age += 1
        print(f"Hapee Birthday {self.name}")


class Student(Person):
    def __init__(self, name, age, course, group):
        super().__init__(name, age)
        self.course = course
        self.group = group

    def student_register(self):
        print(f"Student {self.name} enrolled.")


class Professor(Person):
    def __init__(self, name, age, subject, level):
        super().__init__(name, age)
        self.subject = subject
        self.level = level

    def to_teach(self):
        print(f"Teacher {self.name} started teaching.")


class Employee(Person):
    def __init__(self,name, age, position, department):
        super().__init__(name, age)
        self.position = position
        self.department = department

    def clock_in(self):
        print(f"Employee {self.name} clocked in.")
