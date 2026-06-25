from person import Person

class Professor(Person):
    def __init__(self, name, age, subject, level):
        super().__init__(name, age)
        self.subject = subject
        self.level = level

    def to_teach(self):
        print(f"Teacher {self.name} started teaching.")