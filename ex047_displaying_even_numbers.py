print("The even numbers between 1 and 50 are: ")
for evens in range(0, 51, 2):
    if evens == 50:
        print(f"{evens}.")
    else:
        print(evens, end=', ')


