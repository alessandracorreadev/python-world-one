def int_input(string):
    while True:
        try:
            value = int(input(string))
        except (ValueError, TypeError):
            print("\033[31mError. Enter a valid integer number.\033[m")
        else:
            break
    return value

def float_input(string):
    while True:
        try:
            value = float(input(string))
        except (ValueError, TypeError):
            print("\033[31mError. Enter a valid integer number.\033[m")
        else:
            break
    return value

try:
    n_int = int_input('Enter a integer number: ')
    n_real = float_input('Enter a real number: ')
except KeyboardInterrupt:
    print("\nProgram terminated by the user.")
else:
    print(f"The integer number entered was {n_int} and the real number was {n_real}.")


