count = 0
numb_list = []

while True:
    numb = int(input("Enter a number: "))
    count += 1
    numb_list.append(numb)
    new_numb = ' '
    while new_numb not in 'YyNn':
        new_numb = str(input("Would like to enter another number? [Y/N]: ")).strip()[0]
    if new_numb in 'Nn':
        break

print('-'*50)
print(numb_list)
print(f"You entered {count} numbers.")
print(f"The numbers entered in descending order are: {sorted(numb_list, reverse=True)}")

if 5 in numb_list:
    print("The number 5 is in the list.")
else:
    print("The number 5 is not in the list.")

# use len(numb_list) instead of count