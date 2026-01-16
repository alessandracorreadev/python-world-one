numbers = (int(input("Enter the first number: ")),
           int(input("Enter the second number: ")),
           int(input("Enter the third number: ")),
           int(input("Enter the fourth number: ")))

print(f"The numbers entered were: {numbers}")

if numbers.count(9) == 0:
    print("The number 9 was not entered at all.")
elif numbers.count(9) == 1:
    print(f"The number 9 was entered 1 time.")
else:
    print(f"The number 9 was entered {numbers.count(9)} times.")

if 3 in numbers:
    print(f"The first occurrence of the number 3 is at position {numbers.index(3)+1}.")
else:
    print("There is no number 3 in the list of numbers.")

count = 0
print("The even numbers are: ", end=' ')
for num in numbers:
    count += 1
    if num % 2 == 0:
        if count < 4:
            print(f"{num}, ",end='')
        else:
            print(f"{num}.")

