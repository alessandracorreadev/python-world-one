from hashlib import sha256
from pwinput import pwinput
from rich import print

class BankAccount:
    def __init__(self, id:int, holder:str, key, balance:float = 0):
        self._id = id
        self._holder = holder
        self.__balance = balance
        self.__hash = sha256(key.encode('utf-8')).hexdigest()

    def get_balance(self):
        return self.__balance

    def add_balance(self, value):
        self.__balance += value

    def deduct_balance(self, value):
        self.__balance -= value

    def validate_password(self, key):
        user_key = sha256(key.encode('utf-8')).hexdigest()
        if user_key == self.__hash:
            return True
        else:
            return False

    def attempts(self):
        pass

    def ask_password(self):
        count = 3
        while True:
            password = pwinput(prompt="Enter the password: ", mask="*")
            count -= 1
            if self.validate_password(password):
                return True
            elif count == 0:
                print("[red]Blocked Account[/]")
                break
            else:
                print(f"[red]Invalid password.[/] {count} attempts remaining.")
        return False


    def withdraw(self):
        print('-' * 30)
        print('WITHDRAW'.center(30))
        print('-' * 30)
        while True:
            value = float(input("Enter the value: $"))
            if 0 < value <= self.__balance:
                if self.ask_password():
                    self.deduct_balance(value)
                    print(f"A ${value:.2f} [red]withdraw[/] was completed successfully.")
                    print(f"Current balance: {self.get_balance()}")
                break
            print("[red]Value must be positive or cannot exceed the balance.[/]")

    def deposit(self):
        print('-' * 30)
        print('DEPOSIT'.center(30))
        print('-' * 30)
        while True:
            value = float(input("Enter the value: $"))
            if value > 0:
                self.add_balance(value)
                print(f"A ${value:.2f} [green]deposit[/] was completed successfully.")
                print(f"Current balance: {self.get_balance()}")
                break
            else:
                print("[red]Value must be positive.[/]")


