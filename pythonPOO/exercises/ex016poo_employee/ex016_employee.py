from rich import print
from rich import inspect


class Employee:
    # class attributes
    company = "Caltech"

    # instance attributes
    def __init__(self, name, department, position):
        self.name = name
        self.department = department
        self.position = position

    def introduction(self) -> str:
        return f"Hello, my name is [blue]{self.name}[/], and i'm a {self.position} in the {self.department} department at {Employee.company}. :handshake:"

employee1 = Employee("Sheldon Cooper", "Physics","Theoretical Physicist")
employee2 = Employee("Rajesh Koothrappali", "Physics", "Particle Astrophysicist")

# inspect(employee1)

print(employee1.introduction())
print(employee2.introduction())

print(employee1.empresa)