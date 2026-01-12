num = int(input("Enter a number [or 999 to exit]: "))
num_sum = 0
count = 0

while num != 999:
    num_sum += num
    count += 1
    num = int(input("Enter a number [or 999 to exit]: "))


print(f"The sum of the {count} entered numbers is equal to {num_sum}.")