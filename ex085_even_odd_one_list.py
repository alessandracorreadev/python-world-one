numbers = [[], []]

for c in range(1, 8):
    number = int(input(f"Enter value {c}: "))
    if number % 2 == 0:
        numbers[0].append(number)
    else:
        numbers[1].append(number)

numbers[0].sort()
numbers[1].sort()


print(f"The even numbers entered were: {numbers[0]}")
print(f"The odd numbers entered were: {numbers[1]}")

# In Python, variables do not need to be declared before use.
# They are created automatically when a value is assigned.
# Loops and conditionals do not create a new scope.
