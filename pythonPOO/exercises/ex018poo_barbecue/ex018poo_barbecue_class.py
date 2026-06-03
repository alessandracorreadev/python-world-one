from rich import print
from rich.panel import Panel

class Barbecue:
    meat_person = 0.400
    price_kilo = 82.40

    def __init__(self, title, guests):
        self.guests = guests
        self.title = title

    def __str__(self):
        return f"This is {self.title} with {self.guests} guests."

    def total_meat(self) -> float:
        return Barbecue.meat_person * self.guests

    def total_cost(self) -> float:
        return self.total_meat() * Barbecue.price_kilo

    def cost_person(self) -> float:
        return self.total_cost() / self.guests


    def analyze(self):
        content = f"""Analyzing [green]{self.title}[/] with [blue]{self.guests} guests[/]
Each participant will eat {Barbecue.meat_person:.1f}kg of meat, and each kilogram costs ${Barbecue.price_kilo}
I recommend [blue]buying {self.total_meat():.3f}kg[/] of meat
The total cost will be ${self.total_cost():.2f}
Each person will pay [yellow]${self.cost_person():.2f}[/] to participate"""

        print(Panel(content, title=self.title))

barbecue1 = Barbecue("Friends Barbecue", 15)
barbecue1.analyze()

barbecue2 = Barbecue("Brothers Barbecue", 5)
barbecue2.analyze()

barbecue3 = Barbecue("Family Barbecue", 25)
barbecue3.analyze()