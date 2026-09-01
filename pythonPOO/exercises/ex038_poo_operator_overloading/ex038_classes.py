from rich.console import Console
from rich.text import Text

console = Console()

# guarda uma lista de um mais produtos
# mostra a lista com os produtos adicionados
class Cart:
    def __init__(self):
        self._products = list()

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, item):
        if isinstance(item, Product):
            self._products.append(item)
        elif isinstance(item, Cart):
            self._products += item.products
        else:
            raise TypeError(f"[red]Object type not allowed.[/]")

    def __str__(self):
        products_list = self.products
        total = 0
        content = f"[blue]{'CART':-^24}[/]" + "\n"
        if len(products_list) > 0:
            for product in products_list:
                content += f"{product.name:.<15}${product.price:>7.2f}\n"
                total += product.price
        else:
            content += "Empty cart.\n"
        content += "[blue]-[/]"*24 + "\n"
        content += f"TOTAL: ${total:.2f}"
        return content

    def __add__(self, other):
        self.products = other
        return self

# cria e guarda as informações de um produto
class Product:
    # recebe e guarda o nome e preço do produto
    def __init__(self, name, value):
        self._name = None
        self._price = None
        self.name = name
        self.price = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, product_name:str):
        if len(product_name) < 1:
            raise AttributeError("Name cannot be blank")
        elif len(product_name) == 1:
            raise AttributeError("Name must have more than one letter.")
        else:
            self._name = product_name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        else:
            self._price = value



