from ex115_registration_system.useful import read_int, header, line

def new_r(file):
    header.header("NEW RECORD")
    name = input("Name: ")
    age = read_int.read_int("Age: ")
    with open(file, "a", encoding="utf-8") as f:
        f.write(f"{name};{age}\n")
    line.line()
    print("Registration successful.")
    line.line()