print('-'*50)
print("10 TERMS OF AN ARITHMETIC PROGRESSION".center(50))
print('-'*50)

first_term = int(input("Enter the first term: "))
common_dif = int(input("Enter the value of the common difference: "))
result = first_term

for count in range(1, 11):
    print(f"{result} ", end='') if count == 10 else print(f"{result} → ", end='')
    result += common_dif

print("END")