from ex034_classes import *

employees = [
    Manager("Billy", 8000),
    Designer("Sidney", 6000),
    Developer("Stuart", 7000),
]

def main():
    for employee in employees:
        print(employee)

    Manager.salary = 7500

    print(employees[0])


if __name__ == "__main__":
    main()