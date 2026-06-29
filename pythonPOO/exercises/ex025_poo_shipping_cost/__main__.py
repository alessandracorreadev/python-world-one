from ex025_poo_shipping_cost import *
from rich import print
from rich.table import Table


def main():
    distance = 20

    # delivery1 = Truck(distance)
    # print(f"{type(delivery1).__name__} shipping cost for {distance} km = {delivery1.calculate_shipping()}")

    # delivery2 = Motorcycle(distance)
    # print(f"{type(delivery2).__name__} shipping cost for {distance} km = {delivery2.calculate_shipping()}")

    # delivery3 = Drone(distance)
    # print(f"{type(delivery3).__name__} shipping cost for {distance} km = {delivery3.calculate_shipping()}")

    shipping_list = [Truck(distance), Motorcycle(distance), Drone(distance)]

    shipping_table = Table(title="Shipping Table")

    shipping_table.add_column("Distance")
    shipping_table.add_column("Vehicle")
    shipping_table.add_column("Shipping")

    for line in shipping_list:
        shipping_table.add_row(f"{distance}", f"{type(line).__name__}", f"{line.calculate_shipping()}")

    print(shipping_table)


if __name__ == "__main__":
    main()
