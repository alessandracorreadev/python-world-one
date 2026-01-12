print('-'*50)
print("10 TERMS OF AN ARITHMETIC PROGRESSION".center(50))
print('-'*50)

first_term = int(input("Enter the first term: "))
common_dif = int(input("Enter the value of the common difference: "))
result = first_term
count = 0

while count < 10:
    print(f"{result} → ", end='')
    result += common_dif
    count +=1

print("END.")