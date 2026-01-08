num = int(input("Enter a number to calculate its factorial: "))
factorial = num
result = num
count = 1

print(f"Calculating {num}! = {num} ", end='')


while count < num:
    factorial -= 1
    count += 1
    result *= factorial
    print(f"x {factorial} ", end='')

if result > 1:
    print(f" = {result}")

