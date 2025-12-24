a = float(input("Enter the length of the first line segment: "))
b = float(input("Enter the length of the second line segment: "))
c = float(input("Enter the length of the third line segment: "))

if a + b > c and a + c > b and b + c > a:
    print(f"The meansurements {a}, {b} e {c} form a triangle.")
else:
    print(f"The meansurements {a}, {b} e {c} do not form a triangle.")