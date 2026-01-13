highest = 0
lowest = 0

for people in range(1, 6):
    weight = float(input(f"Enter the weight of person {people}: "))
    if people == 1:
        highest = weight
        lowest = weight
    else:
        if weight > highest:
            highest = weight
        if weight < lowest:
            lowest = weight

print(f"The lowest reported weight is {lowest}.")
print(f"The highest reported weight is {highest}.")
