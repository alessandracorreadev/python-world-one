num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

options = ('''Do you want to: 
[1]Add
[2]Multiply
[3]Show the greater value
[4]Enter new numbers
[5]Exit the program''')

choice = 0

while choice != 5:
    print(options)
    choice = int(input("Enter your option: "))

    if choice == 1:
        print(f"The sum of the values {num1} and {num2} is equal to {num1+num2}.")
    elif choice == 2:
        print(f"The multiplication of the values {num1} and {num2} is equal to {num1*num2}.")
    elif choice == 3:
        if num1 > num2:
            print(f"The greatest value entered is {num1}.")
        elif num2 > num1:
            print(f"The greatest value entered is {num2}.")
        else:
            print(f"The entered values are equal.")
    elif choice == 4:
        print('-' * 50)
        num1 = int(input("Enter the new first number: "))
        num2 = int(input("Enter the new second number: "))
    else:
        print("Invalid option.")

    print('-' * 50)

print("You have exited the program.")
