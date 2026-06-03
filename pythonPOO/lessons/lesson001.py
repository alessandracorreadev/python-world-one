class Person:
    def __init__(self):
        # attributes
        self.name = ""
        self.age = 0

    def birthday(self):
        self.age = self.age + 1

    def bday_message(self):
        return f"{self.name} is a person and is {self.age} years old."


p1 = Person()
p1.name = "Sheldon Cooper"
p1.age = 27
p1.birthday()
print(p1.bday_message())

p2 = Person()
p2.name = "Leonard Hofstadter"
p2.age = 27
print(p2.bday_message())