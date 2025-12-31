weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height**2)

print(f"Your BMI is {bmi:.1f}, ", end='')

if bmi < 18.5:
    print("you are underweight.")
elif 18.5 <= bmi < 25:
    print("congratulations, you are at a healthy weight!")
elif 25 <= bmi < 30:
    print("you are overweight.")
elif 30 <= bmi < 40:
    print("you are obese.")
else:
    print("you have morbid obesity. Warning!")