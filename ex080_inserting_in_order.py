numbers_list = []

for count in range(0, 5):
    n = int(input(f"Enter a number: "))
    if count == 0:
        numbers_list.append(n)
        print("The number was added to the end of the list...")
    else:
        if n > max(numbers_list):
            numbers_list.append(n)
            print("The number was added to the end of the list...")
        else:
            new_position = 0
            for position, number in enumerate(numbers_list):
                if n > number:
                    new_position = position+1
            numbers_list.insert(new_position, n)
            print(f"The number was added at position {new_position} in the list...")


print(f"The list of numbers entered was: {numbers_list}")
