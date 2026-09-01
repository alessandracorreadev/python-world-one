from pythonPOO.exercises.ex031_poo_rectangle.class_rectangle import Rectangle
from rich import print

def main():
    # --------------------------------
    # r1 = Rectangle(3, 8)
    # --------------------------------
    # r1 = Rectangle()
    # r1.base = 12
    # r1.height = 4
    # -------------------------------
    try:
        r1 = Rectangle()
        r1.dimensions = (4, 9)

    except Exception as error:
        print(f"Error type: [red]{type(error).__name__}[/]({error})")

    print(r1.dimensions)

if __name__ == "__main__":
    main()