from pythonPOO.exercises.ex033_poo_student.student_class import Person, Student
from rich import print, inspect

def main():
    try:
        s1 = Student("Cornelia", 1998, "Fashion Design")
        print(s1.name)
        print(s1.age)
        print(s1.course)
        s1.course = "Data Engineer"
        Student.add_course("Data Science")
        s1.course = "Data Engineer"
        Student.add_course("data science")
        Student.add_course("data engineer")
        print(Student.degree_list)
    except Exception as error:
        print(f"[red]An error occurred:[/] {error}")

if __name__ == "__main__":
    main()
