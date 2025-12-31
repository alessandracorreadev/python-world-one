from time import sleep

price = float(input("What is the value of the property? R$"))
salary = float(input("What is the buyer's salary? R$"))
years = int(input("How many years would you like to take to pay for the house? "))

print("Analyzign your loan...")
sleep(2)

months = years * 12

installment = price / months

print(f"The installment amount is ${installment:.2f}.")
if installment <= (salary * 0.3):
    print("Your loan has been approved.")
else:
    print("Your loan was not approved.")