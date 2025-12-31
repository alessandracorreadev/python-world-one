a = float(input("Enter the length of the first line segment: "))
b = float(input("Enter the length of the second line segment: "))
c = float(input("Enter the length of the third line segment: "))

if a + b > c and a + c > b and b + c > a:
    print(f"The meansurements {a}, {b} e {c} form ", end='')
    if a == b == c:
        print("an equilateral triangle.")
    elif a != b != c != a:
        print("a right triangle.")
    else:
        print("an isosceles triangle.")
else:
    print(f"The meansurements {a}, {b} e {c} do not form a triangle.")

