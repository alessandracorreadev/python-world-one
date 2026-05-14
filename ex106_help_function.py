

from time import sleep
def help_function(name):
    return help(name)

def system_title(title):
    lenght = len(title)+4
    print("~" * lenght)
    print(f"  {title}  ")
    print("~" * lenght)
    sleep(1)

while True:
    system_title("PYTHON HELP SYSTEM - PYHELP")
    user_answer = input("Enter a Method or a Library > ").lower()
    if user_answer == "end":
        break
    system_title(f"Accessing the manual for the '{user_answer}' command...")
    help_function(user_answer)

system_title("SEE YOU SOON.")