def create_file(file_name):
    with open(file_name, "x", encoding="utf-8") as file:
        pass
    print("File created successfully.")
