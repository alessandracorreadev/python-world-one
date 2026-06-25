from rich import print, inspect

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

s1 = Student("Howard Wolowitz", 26, "Analytical Mechanics physics", "C073")
s1.happy_bday()
s1.student_register()
inspect(s1, methods=True)

t1 = Professor("Sheldon Cooper", 27, "Theoretical Physics", "University")
t1.happy_bday()
inspect(t1, methods=True)

e1 = Employee("Rajesh Koothrappali", 25, "Astrophysicist", " Physics and Astronomy")
e1.clock_in()
inspect(e1)