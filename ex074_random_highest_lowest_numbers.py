from random import  randint

n1 = randint(0, 10)
n2 = randint(0, 10)
n3 = randint(0, 10)
n4 = randint(0, 10)
n5 = randint(0, 10)

numbers = (n1, n2, n3, n4, n5)

print(f"The generated numbers were: {numbers}.")
highest = numbers[0]
lowest = numbers[0]

for num in numbers:
    if num > highest:
        highest = num
    if num < lowest:
        lowest = num

print(f"The lowest number generated was {lowest}.")
print(f"The highest number generated was {highest}.")

print(f"The lowest number generated was {max(numbers)}.")
print(f"The highest number generated was {min(numbers)}.")