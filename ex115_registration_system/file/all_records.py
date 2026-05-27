from ex115_registration_system.useful import read_int, header, line

def all_records(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            try:
                record_list = f.readlines()
            except:
                print(f"Error reading the file: {file}")
            else:
                for record in record_list:
                    formated_rec = record.strip().split(';')
                    print(f"{formated_rec[0]}".ljust(35), end='')
                    print(f"{formated_rec[1]} years old".ljust(15))
    except:
        print("Error: file or directory not found.")

