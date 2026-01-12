count = 0
sum_num = 0
while True:
    num = int(input("Enter a number: "))
    if num == 999:
        break
    count += 1
    sum_num += num

print(f"The sum of the {count} entered numbers is equal to {sum_num}.")
