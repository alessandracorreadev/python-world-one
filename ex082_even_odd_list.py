numb_list = []
even = []
odd = []

while True:
    numb = int(input("Enter a number: "))
    numb_list.append(numb)
    if numb % 2 == 0:
        even.append(numb)
    else:
        odd.append(numb)
    new_numb = ' '
    while new_numb not in 'YyNn':
        new_numb = str(input("Would like to enter another number? [Y/N]: ")).strip()[0]
    if new_numb in 'Nn':
        break

print('-'*50)
print(f"The complet list: {numb_list}")
print(f"Even numbers list: {even}")
print(f"Odd numbers list: {odd}")
