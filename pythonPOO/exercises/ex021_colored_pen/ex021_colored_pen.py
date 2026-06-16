from rich import print
from rich import emoji

class Pen:
    def __init__(self, color = "grey"):
        self.color = color.lower().strip()
        self.capped = False

    def line_break(self, number=1):
        print("\n"*number)

    def uncap(self):
        self.capped = True

    def cap(self):
        self.capped = False

    def write(self, message):
        if self.capped:
            print(f"[{self.color}]{message}[/]", end='')
        else:
            print(f":prohibited: The pen is capped.")


pen1 = Pen("blue")
pen2 = Pen("Red  ")
pen3 = Pen()

pen1.write("This is a blue pen.")

pen1.uncap()
pen2.uncap()
pen3.uncap()

pen1.write("This is a blue pen.")
pen1.line_break()
pen2.write("This is a red pen.")
pen2.line_break(3)
pen3.write("This is a default color pen.")

