from rich import print, inspect
from lesson008_abstraction_classes import Student, Employee, Professor, Person

s1 = Student("Howard Wolowitz", 26, "Analytical Mechanics Physics", "C073")
s1.happy_bday()
s1.student_register()
s1.study()
#inspect(s1, methods=True)

t1 = Professor("Sheldon Cooper", 27, "Analytical Mechanics Physics", "University")
t1.happy_bday()
t1.study()
#inspect(t1, methods=True)

e1 = Employee("Rajesh Koothrappali", 25, "Astrophysicist", " Physics and Astronomy")
e1.study()
e1.clock_in()
#inspect(e1)

