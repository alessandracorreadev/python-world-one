from ex115_registration_system.useful import line, colors


def header(text):
    line.line()
    print(f"{colors.colors['bold']}{text.center(50)}{colors.colors['reset']}")
    line.line()
