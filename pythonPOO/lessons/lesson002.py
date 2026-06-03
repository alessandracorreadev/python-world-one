class Person:
    """
    Represents a person.
    To create a new person, use:
    variable = Person(name, age)
    """
    def __init__(self, name="empty", age=0):
        # attributes
        self.name = name
        self.age = age

    def birthday(self):
        self.age = self.age + 1

    def bday_message(self):
        return f"{self.name} is a person and is {self.age} years old."

    # def __str__(self):
        # return f"{self.name} is a person and is {self.age} years old."

    def __getstate__(self):
        return f"State: name = {self.name} ; age = {self.age}"


p1 = Person("Sheldon Cooper", 27)
p1.birthday()
print(p1.bday_message())

p2 = Person("Leonard Hofstadter", 27)
print(p2.bday_message())

p3 = Person()
print(p3.bday_message())

print(Person.__doc__)

# returns object information and can be customized with def __str__(self): return ...
print(p1)

print(p1.__dict__)
print(p1.__getstate__())

print(p1.__class__)