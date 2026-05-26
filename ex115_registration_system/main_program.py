from ex115_registration_system.file import file_validation, create_file
from ex115_registration_system.interface import user_input
from ex115_registration_system.useful import header

file_name = 'records.txt'

if not file_validation.file_validator(file_name):
    create_file.create_file(file_name)

user_options = ['View all records', 'Register a new person', 'Exit the system']

try:
    user_input.user_input(user_options, file_name)
except KeyboardInterrupt:
    print()
    header.header("EXIT BY THE USER")

