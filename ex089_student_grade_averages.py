all_grades = []

while True:
    # getting the student's name and two grades
    name = input("Enter the student's name: ")
    grade_1 = float(input("Grade 1: "))
    grade_2 = float(input("Grade 2: "))

    # compute average
    average = (grade_1 + grade_2) / 2

    all_grades.append([name, average, [grade_1, grade_2]])

    # continue question
    new_student = ' '
    while new_student not in 'YyNn':
        new_student = input("Continue? [Y/N]: ").strip().lower()[0]
    if new_student in 'Nn':
        break

print('-='*40)

print(f"{"No.":<4}{"NAME":<12}{"AVERAGE":>8}")
print('-'*28)
for i, student in enumerate(all_grades):
    print(f"{(i+1):<4}{student[0].capitalize():<12}{student[1]:>7.1f}")
print('-'*28)

while True:
    student_no = int(input("Enter the student number to view grades or [999] to exit: ")) - 1
    if student_no == 999 - 1:
        break
    elif 0 <= student_no <= len(all_grades) -1:
        print(f"Grades for {all_grades[student_no][0].capitalize()}: {all_grades[student_no][2]}")
    else:
        print("Invalid option.")
    print('-' * 28)