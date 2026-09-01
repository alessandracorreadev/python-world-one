from ex038_classes import *

def main():
    p1 = Product("T-shirt", 50)
    p2 = Product("Skirt", 75)
    p3 = Product("Sweater", 110.90)

    c1 = Cart()
    # print(c1)
    # c1.products = p1
    # c1.products = p3
    # c1.products = p2
    c1 = c1 + p1
    console.print(Text.from_markup(str(c1)))
    p1.price = 45
    console.print(Text.from_markup(str(c1)))
    c2 = Cart()
    c2 = c2 + p3 + c1
    console.print(Text.from_markup(str(c2)))

if __name__ == "__main__":
    main()
