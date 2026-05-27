from ex115_registration_system.useful import line


def new_r(file, name='unknown', age=0):
    try:
        with open(file, "a", encoding="utf-8") as f:
            try:
                f.write(f"{name};{age}\n")
            except:
                print(f"Error writing to file: {file}")
            else:
                line.line()
                print("Registration successful.")
                line.line()
    except:
        print("Error: file or directory not found.")
