from ex024_poo_coffee_machine import *

def main():
    e1 = Espresso()
    e1.prepare()

    t1 = Tea()
    t1.prepare()

    l1 = Latte()
    l1.prepare()

if __name__ == "__main__":
    main()