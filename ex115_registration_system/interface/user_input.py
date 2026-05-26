from ex115_registration_system.interface import interactive_menu
from ex115_registration_system.useful import colors, header, read_int
from ex115_registration_system.file import new_record, all_records
from time import sleep

def user_input(options,file_name):
    while True:
        interactive_menu.menu(options)
        while True:
            user_opt = read_int.read_int("Enter your option: ")
            if user_opt == 1:
                # return de file records.txt content
                all_records.all_records(file_name)
                break
            elif user_opt == 2:
                # register a new person in records.txt
                new_record.new_r(file_name)
                break
            elif user_opt == 3:
                break
            else:
                print(f"{colors.colors["red"]}Error: Enter a valid option.{colors.colors["reset"]}")
        if user_opt == len(options):
            break
        sleep(1.5)
    header.header("EXIT BY THE USER")

