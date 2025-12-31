from datetime import date

birth_year = int(input("Enter your birth year: "))

actual_year = date.today().year

age = actual_year - birth_year

print(f"You have {age} years old.")

if age < 18:
    print("It is not time to enlist in the military yet.")
    print(f"There are {18 - age} years left until your enlistment.")
elif age == 18:
    print("It is time to elist in the military.")
else:
    print("The time to enlist in the military has already passed.")
    print(f"You should have enlisted {age - 18} years ago.")
