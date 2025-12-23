# using int
print('*'*30)
print("Using Numbers")

num = int(input("Enter a number between 0 and 9999: "))

thousand = (num // 1000)
hundred = (num % 1000) // 100
ten = (num % 100) // 10
unit = (num % 10)

print(f"Unit: {unit}")
print(f"Ten: {ten}")
print(f"Hundred: {hundred}")
print(f"Thousand: {thousand}")

# using string
print('*'*30)
print("Using Strings")

num = input("Enter a number between 0 and 9999: ").strip().rjust(4, '0')
print('.'+ num + '.') # print for test

print(f"Unit: {num[3]}")
print(f"Ten: {num[2]}")
print(f"Hundred: {num[1]}")
print(f"Thousand: {num[0]}")

