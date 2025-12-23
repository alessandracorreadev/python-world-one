from math import sqrt, pow, hypot, ceil

leg_op = float(input("Enter teh length of the opposite leg: "))
leg_ad = float(input("Enter the length of the adjacent leg: "))
hypo = ((leg_op ** 2)+(leg_ad ** 2)) ** (1/2)
hypo1 = sqrt((pow(leg_op, 2))+(pow(leg_ad, 2)))
hypo2 = hypot(leg_ad, leg_op)

print(f"The hypotenuse will measure {hypo1:.2f}.")
