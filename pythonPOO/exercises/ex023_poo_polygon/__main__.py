from rich import print, inspect

from ex023_poo_polygon import *

def main():
    s1 = Square(12)

    print(f"Perimeter = {s1.perimeter():.1f}")
    print(f"Area = {s1.area():.1f}")
    inspect(s1, methods=True)
    print('-'*30)

    c1 = Circle(12)

    print(f"Perimeter = {c1.perimeter():.1f}")
    print(f"Area = {c1.area():.1f}")
    print('-'*30)

    t1 = Triangle(3, 4, 5)
    print(f"Perimeter = {t1.perimeter():.1f}")
    print(f"Area = {t1.area():.1f}")
    print('-'*30)

if __name__ == "__main__":
    main()