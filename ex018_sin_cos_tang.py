from math import sin, cos, tan, radians

angle = float(input("Enter the angle you want: "))
radians = radians(angle)

sine = sin(radians)
cosine = cos(radians)
tangent = tan(radians)

print(f"The angle of {angle}° has a sine of {sine:.2f}.")
print(f"The angle of {angle}° has a cosine of {cosine:.2f}.")
print(f"The angle of {angle}° has a tangent of {tangent:.2f}.")