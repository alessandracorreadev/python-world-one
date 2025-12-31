num = int(input("Enter a number: "))

print(f"Would you like to convert the number {num} to:")
print('''[1] Binary
[2] Octal
[3] Hexadecimal''')

choice = int(input("Enter your answer: "))

if choice == 1:
    print(f"The number {num} in binary is equal to {bin(num)[2:]}.")
elif choice == 2:
    print(f"The number {num} in binaryis equal to {oct(num)[2:]}.")
elif choice == 3:
    print(f"The number {num} in binary is equal to {hex(num)[2:]}.")
else:
    print(f"Invalid option.")