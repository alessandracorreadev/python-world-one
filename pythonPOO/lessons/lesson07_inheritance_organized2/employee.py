from person import Person

class Employee(Person):
    def __init__(self,name, age, position, department):
        super().__init__(name, age)
        self.position = position
        self.department = department

    def clock_in(self):
        print(f"Employee {self.name} clocked in.")