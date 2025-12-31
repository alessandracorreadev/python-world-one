from datetime import date

birth_year = int(input("Enter your birth year: "))
actual_year = date.today().year
age = actual_year - birth_year

print(f"The athlete is {age} years old.")

if age <= 9:
    print("Classification: MIRIN.")
elif age <= 14:
    print("Classification: YOUTH.")
elif age <= 19:
    print("Classification: JUNIOR.")
elif age <= 25:
    print("Classification: SENIOR.")
else:
    print("Classification: MASTER.")
