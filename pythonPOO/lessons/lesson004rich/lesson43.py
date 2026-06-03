from rich import print
from rich.table import Table

table = Table(title="Price Table")

table.add_column("Name", justify="right", style="cyan")
table.add_column("Price")
table.add_row("Pencil", "$10,50")
table.add_row("Journal", "$50.20")
print(table)