from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def happy_bday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}.")

    # use @abstractmethod to define a common interface that all concrete subclasses must implement.
    @abstractmethod
    def study(self):
        pass

class Student(Person):
    def __init__(self, name, age, course, group):
        super().__init__(name, age)
        self.course = course
        self.group = group

    def student_register(self):
        print(f"Student {self.name} enrolled.")

    def study(self):
        print(f"{self.name} is studying {self.course} in class {self.group}.")


class Professor(Person):
    def __init__(self, name, age, subject, level):
        super().__init__(name, age)
        self.subject = subject
        self.level = level

    def to_teach(self):
        print(f"Teacher {self.name} started teaching.")

    def study(self):
        print(f"{self.name} is not studying, is teaching {self.subject}.")


class Employee(Person):
    def __init__(self,name, age, position, department):
        super().__init__(name, age)
        self.position = position
        self.department = department

    def clock_in(self):
        print(f"Employee {self.name} clocked in.")

    def study(self):
        print(f"{self.name} is not studyin, is working as {self.position}.")
