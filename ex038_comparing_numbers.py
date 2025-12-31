from time import sleep

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Analyzing your numbers...")
sleep(1)

if num1 > num2:
    print(f"The number {num1} is greater than {num2}.")
elif num2 > num1:
    print(f"The number {num2} is greater than {num1}.")
else:
    print(f"There is no greater number. The values {num1} and {num2} are equal.")