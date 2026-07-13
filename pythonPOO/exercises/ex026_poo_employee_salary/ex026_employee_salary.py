from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Employee(ABC):
    min_salary = 1612
    tax = 7.5

    def __init__(self, name= None):
        self.name = name
        self.gross_salary = 0
        self.salary = 0

    @abstractmethod
    def calculate_salary(self):
        pass

    def analyze_salary(self):
        base = self.salary/self.min_salary

        text = (f"[blue]{self.name}[/] ([purple]{self.__class__.__name__}[/]) earns [green]${self.salary:.2f}[/], "
                f"which is equivalent to [yellow]{base:.1f} minimum wages[/]")
        print(Panel(text, title="Analyze Salary", width=44))

class HourlyEmployee(Employee):
    def __init__(self, name, hours_worked=220, hourly_rate=7.37):
        super().__init__(name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.gross_salary = self.hourly_rate * self.hours_worked

    def calculate_salary(self):
        self.salary = self.gross_salary - (self.gross_salary * Employee.tax/100)


class SalariedEmployee(Employee):
    def __init__(self, name, gross_salary):
        super().__init__(name)
        self.gross_salary = gross_salary

    def calculate_salary(self):
        self.salary = self.gross_salary - (self.gross_salary * (self.tax/100))


