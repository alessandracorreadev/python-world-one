from rich import print, inspect
from classes007 import Student, Professor, Employee

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

