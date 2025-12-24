salary = float(input("Enter your salary amount: "))
new_salary = 0

if salary > 1250:
    new_salary = salary + (salary * 0.1)
    print(f"You received a 10% raise. Your salary is now ${new_salary:.2f}.")
else:
    new_salary = salary + (salary * 0.15)
    print(f"You received a 15% raise. Your salary is now ${new_salary:.2f}.")