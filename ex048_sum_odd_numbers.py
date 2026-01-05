odd_sum = 0

for odd in range(1, 501, 2):
    if odd % 3 == 0:
        odd_sum += odd

print(f"The sum of odd numbers that are multiples of 3 between 1 and 500 is: {odd_sum}.")