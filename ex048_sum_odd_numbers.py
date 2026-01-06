odd_sum = 0
count = 0

for odd in range(1, 501, 2):
    if odd % 3 == 0:
        odd_sum += odd
        count += 1

print(f"The sum of all {count} odd numbers that are multiples of 3 between 1 and 500 is: {odd_sum}.")