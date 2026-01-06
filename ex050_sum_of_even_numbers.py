sum_even = 0
count_even = 0

for count in range(1, 7):
    n = int(input(f"Enter the {count}º number: "))
    if n % 2 == 0:
        sum_even += n
        count_even += 1

if count_even == 1:
    print(f"You entered only the even number {sum_even}.")
else:
    print(f"The sum of the entered even numbers is equal to {sum_even}.")