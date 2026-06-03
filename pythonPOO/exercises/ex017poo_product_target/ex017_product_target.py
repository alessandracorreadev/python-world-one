from rich import print
from rich.panel import Panel

class Product:
    title = "Products"

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def target(self):
        formatted_price = f"${self.price:,.2f}"
        content = f"{self.name:^30}\n" + "-"*30 + f"\n{formatted_price:.^30}"
        print(Panel(f"{content}", title=f"{Product.title}", width=36))


product1 = Product("MacBook Air M4", 13_000.00)
product2 = Product(" iPad com chip A16", 3_799.00)

product1.target()
product2.target()

