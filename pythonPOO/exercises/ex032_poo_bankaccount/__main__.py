from pwinput import pwinput
from pythonPOO.exercises.ex032_poo_bankaccount.class_bankaccount import BankAccount
from rich import print, inspect

def main():
    name = input("Enter the name: ")
    password = pwinput(prompt="Enter the password: ", mask="*")
    account1 = BankAccount(1, name, password)
    # inspect(account1, methods=True, private=True)
    account1.deposit()
    account1.withdraw()
    account1.name = "Maria"

if __name__ == "__main__":
    main()