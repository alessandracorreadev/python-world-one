from rich import inspect

class BankAccount:
    """
     Represents a bank account and  allows deposits and withdrawals
    """

    def __init__(self, id, name, balance=0):
        self.id = id
        self.holder = name
        self.balance = balance

    def __str__(self):
        return f"Account {self.id} - Account Holder: {self.holder} - Balance: ${self.balance:,.2f}"

    def deposit(self, value):
        self.balance += value
        print(f"Deposit of ${value:,.2f} authorized for account {self.id}.")

    def withdrawals(self, value):
        if value > self.balance:
            print(f"Insufficient funds.")
        else:
            self.balance -= value
            print(f"Withdrawal of ${value:,.2f} authorized for account {self.id}.")

account1 = BankAccount(73, "Sheldon Cooper", 5000)

print(account1)
print(account1.__doc__)
account1.deposit(500)
print(account1)
account1.withdrawals(7000)
account1.withdrawals(300)

inspect(account1)