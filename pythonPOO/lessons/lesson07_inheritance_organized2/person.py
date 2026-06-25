class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def happy_bday(self):
        self.age += 1
        print(f"Hapee Birthday {self.name}")