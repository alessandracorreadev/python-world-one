from ex115_registration_system.useful import colors, header, line


def menu(show_options):
    header.header("MAIN MENU")
    for ind, opt in enumerate(show_options):
        print(f"{colors.colors["yellow"]} {ind + 1} - {colors.colors["blue"]}{opt}{colors.colors["reset"]}")
    line.line()
