from datetime import date
from time import sleep

employee = dict()

employee['name'] = str(input("Enter the employee's name: "))
birth_year = int(input("Enter the birth year: "))
age = date.today().year - birth_year
employee['age'] = age
employee['work permit'] = int(input("Work permit number[ or 0 if none]: "))
if employee['work permit'] != 0:
    employee['hiring year'] = int(input("Year of hire: "))
    employee['salary'] = float(input("Salary: $"))
    retirement = (employee['hiring year'] + 35) - birth_year
    employee['retirement'] = retirement


print('-'*50)
for data in employee.items():
    print(f"  - The {data[0]} has a value of {data[1]}")
    sleep(1)


