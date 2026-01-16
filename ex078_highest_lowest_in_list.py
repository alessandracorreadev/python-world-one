numbers = []

for n in range(0, 5):
    numbers.append(int(input(f"Enter a number for position {n}: ")))

print(f"You entered the numbers: {numbers}.")

highest = max(numbers)
lowest = min(numbers)

print(f"The highest number entered was {highest} in positions: ", end='')
for position, number in enumerate(numbers):
    if number == highest:
        print(f"{position}...", end='')

print()

print(f"The lowest number entered was {lowest} in positions: ", end='')
for position, number in enumerate(numbers):
    if number == lowest:
        print(f"{position}...", end='')