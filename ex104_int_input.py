def int_input(string):
    while True:
        value = input(string)
        if value.isnumeric():
            break
        print("\033[31mError. Enter a valid integer.\033[m")
    return value


n = int_input('Enter a number: ')
print(f"You just entered the number {n}.")

