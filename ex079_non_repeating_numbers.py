numbers = []

while True:
    n = int(input(f"Enter a number: "))
    if n not in numbers:
        numbers.append(n)
        print("Number added successfully.")
    else:
        print("Duplicate value. I will not add it.")
    new_number = ' '
    while new_number not in 'yYNn':
        new_number = input("Dou you want to add another number? [Y/N]: ").strip().lower()[0]
    if new_number in 'nN':
        break

print('-'*50)
print(f"You entered the numbers: {numbers}")