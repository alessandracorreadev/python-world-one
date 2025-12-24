num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter the last number: "))

largest = num1
smallest = num1

if num2 > num1 and num2 > num3:
    largest = num2

if num3 > num1 and num3 > num2:
    largest = num3

if num2 < num1 and num2 < num3:
    smallest = num2

if num3 < num1 and num3 < num2:
    smallest = num3


print(f"The largest number is {largest}")
print(f"The smallest number is {smallest}")