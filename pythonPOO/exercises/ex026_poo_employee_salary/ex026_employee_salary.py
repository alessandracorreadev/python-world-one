from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Employee(ABC):
    def __init__(self, name, gross_salary=0):
        self.name = name
        self.gross_salary = gross_salary
        self.salary = 0
        self.min_salary = 1612
        self.tax = 7.5

    @abstractmethod
    def calculate_salary(self):
        pass

    def analyze_salary(self):
        text = (f"[blue]{self.name}[/] ([purple]{self.__class__.__name__}[/]) earns [green]${self.salary:.2f}[/], "
                f"which is equivalent to [yellow]{self.salary/self.min_salary:.1f} minimum wages[/]")
        print(Panel(text, title="Analyze Salary", width=44))


class HourlyEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        self.gross_salary = self.hourly_rate * self.hours_worked
        self.salary = self.gross_salary - (self.gross_salary * (self.tax/100))


class SalariedEmployee(Employee):
    def calculate_salary(self):
        self.salary = self.gross_salary - (self.gross_salary * (self.tax/100))
        return f"${self.salary:.2f}"

