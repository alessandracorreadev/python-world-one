from rich import print
from rich.panel import Panel
from ex026_employee_salary import *

def main():
    e1 = HourlyEmployee("Paul", 12, 200)
    e1.calculate_salary()
    e1.analyze_salary()

    e2 = SalariedEmployee("Amanda", 9500)
    e2.calculate_salary()
    e2.analyze_salary()

if __name__ == "__main__":
    main()