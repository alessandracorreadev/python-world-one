numb = int(input("Enter a number: "))
green = "\033[32m"
reset = "\033[0m"
count = 0

for c in range(1, numb+1):
    if numb % c == 0:
        # print(f"{green}{c}{reset}", end=' ')
        count += 1
    # else:
        # print(f"{c}", end=' ')

# print()

if count == 2:
    print(f"The number {numb} is a prime number.")
else:
    print(f"The number {numb} is not a prime number.")