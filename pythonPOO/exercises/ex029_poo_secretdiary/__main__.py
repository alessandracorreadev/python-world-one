from pythonPOO.exercises.ex029_poo_secretdiary.secret_diary import *
from rich import print

def main():
    d = Diary()
    d.write("This message is a secret.")
    d.write("If you can read this your code is ok.")
    try:
        # d.read()
        d.read("P@55w0rd")
    except:
        print("[red]Wrong password.[/]")

if __name__ == "__main__":
    main()
