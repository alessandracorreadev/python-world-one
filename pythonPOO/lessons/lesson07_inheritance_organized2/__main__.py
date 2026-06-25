from rich import print, inspect
from student import Student
from professor import Professor
from employee import Employee

def main():
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

if __name__ == "__main__":
    main()