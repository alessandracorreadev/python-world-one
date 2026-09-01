import locale
from abc import ABC
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

class Payment(ABC):
    def __init__(self):
        self._value = None
        self._f_currency = None

    @property
    def f_currency(self):
        return self._f_currency

    @f_currency.setter
    def f_currency(self, value):
         self._f_currency = locale.currency(self.value, grouping=True, symbol=True)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, user_input:float):
        if not self._value:
            if user_input < 1:
                raise ValueError("Value cannot be zero ou negative.")
            else:
                self._value = user_input
            self.f_currency = self._value
        else:
            raise AttributeError("You cannot change the payment value. Create a new payment.")


    def pay(self, value):
        self.value = value
        print(f"Payment of {self.f_currency} confirmed via ",end='')

class BankSlip(Payment):
    def __init__(self):
        super().__init__()

    def pay(self, value):
        super().pay(value)
        print("Bank Slip.")


class Pix(Payment):
    def __init__(self):
        super().__init__()

    def pay(self, value):
        super().pay(value)
        print("PIX.")

class CreditCard(Payment):
    def __init__(self):
        super().__init__()

    def pay(self, value):
        super().pay(value)
        print("Credit Card.")


def complete_purchase(payment_type, value):
    payment_type.pay(value)