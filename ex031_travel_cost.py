distance = float(input("Enter the trip distance in km: "))
cost = 0

if distance <= 200:
    cost = distance * 0.5
    print(f"The ticket cost for this trip is ${cost:.2f}.")
else:
    cost = distance * 0.45
    print(f"The ticket cost for this trip is ${cost:.2f}")

