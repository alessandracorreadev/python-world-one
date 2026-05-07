def area(w, l):
    a = w * l
    print(f"The area of a {w} x {l} meter plot is {a:.2f} square meters.")

print('-'*50)
print('CALCULATING THE AREA OF A PLOT IN METERS'.center(50))
print('-'*50)
print("Enter the land dimensions.".center(50))
width = float(input("Width (m): "))
length = float(input("Length (m): "))

area(width, length)
print('-'*50)
