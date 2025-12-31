grade1 = float(input("Enter de first grade: "))
grade2 = float(input("Enter de second grade: "))

average = ( grade1 + grade2 ) / 2

print(f"Your average is {average:.1f}, ", end='')

if average < 5:
    print("you have failed!")
elif 5 <= average < 7:
    print(f"uou are in recovery.")
else:
    print("you have passed!")