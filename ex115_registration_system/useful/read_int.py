from ex115_registration_system.useful import colors


def read_int(msg):
    while True:
        try:
            number = int(input(msg))
        except (ValueError, TypeError):
            print(f"{colors.colors["red"]}Error: enter a valid integer number.{colors.colors["reset"]}")
        else:
            break
    return number