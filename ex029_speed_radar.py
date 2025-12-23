speed = float(input("Enter the car's speed in (km/h): "))

if speed > 80:
    fine = (speed - 80) * 7
    print(f"Your speed is {speed}km/h and exceeded 80km/h. You have been fined!")
    print(f"Ther fine amount is ${fine:.2f}.")
else:
    print("Your are within the allowed speed limit.")