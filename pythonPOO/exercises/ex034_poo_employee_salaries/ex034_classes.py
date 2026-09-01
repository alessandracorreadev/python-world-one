from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name:str, salary:float):
        self.__name = name
        self.__salary = salary

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name:str):
        if not new_name or not new_name.strip():
            raise ValueError("Name cannot be empty.")
        elif len(new_name.strip()) < 2:
            raise ValueError("The name must have more than one letter.")
        else:
            self.__name = new_name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value:float):
        if value < 0:
            raise ValueError("The salary cannot be negative.")
        else:
            self.__salary = value

    @abstractmethod
    def calculate_bonus(self):
        pass

    def __str__(self):
        return f"{self.name} is a {self.__class__.__name__} and has a R${self.calculate_bonus():.2f} bonus salary."


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return self.salary * 0.15

class Designer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return self.salary * 0.8

class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return self.salary * 0.10

