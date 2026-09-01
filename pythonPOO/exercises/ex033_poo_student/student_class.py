# Person class that stores a name, birth year, and age.
# Student class that inherits from Person and stores a course.
# The student's age can be accessed but cannot be modified. (raises an error)
# The student's birth year can be updated
# The student's course can be changed if it exists in the course list
# New courses can be added to de course list

from abc import ABC
from datetime import date
from rich import print

class Person(ABC):
    def __init__(self, name, birth):
        self._name = name
        self._birth = birth

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or len(new_name) < 3:
            raise TypeError("Enter a valid name.")
        if not new_name.isalpha():
            raise ValueError("A name must contain only letters.")
        else:
            self._name = new_name

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, year):
        if not isinstance(year, int):
            raise TypeError("The year must be an integer number.")
        if not len(str(year)) == 4:
            raise ValueError("The year must have 4 digits.")
        else:
            self._birth = year

    @property
    def age(self):
        return date.today().year - self._birth

    @age.setter
    def age(self, value):
        raise TypeError("You cannot change the age. Change the birth year instead.")


class Student(Person):
    # This list is a class attribute because it is shared by all instances.
    degree_list = ["Computer Science", "Software Engineering", "Fashion Design", "Graphic Design",
                   "Businnes Administration"]

    def __init__(self, name, birth, course):
        super().__init__(name, birth)
        self._course = None
        self.course = course

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, name_course):
        if name_course in self.degree_list:
            self._course = name_course
        else:
            print(f"[red]The course [green]{name_course}[/] is not in the list. [/]Please choose a valid option: ")
            for pos, c in enumerate(self.degree_list):
                print(f"{pos+1}. {c}")

    @classmethod
    def add_course(cls, name):
        if not isinstance(name, str) or not name.replace(" ", "").isalpha():
            raise TypeError("A course name must have only letters.")
        if len(str(name)) < 3:
            raise ValueError("Too short for a course name.")
        if str(name.title()) in cls.degree_list:
            print(f"The course [green]{str(name.title())}[/] is already in the list.")
        else:
            cls.degree_list.append(name.title())



