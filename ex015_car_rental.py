days = int(input("How many days was it rented for? "))
km = float(input("How many kilometers were driven? "))

total_amount = (days * 60) + (km * 0.15)

print(f"The total amount to pay is ${total_amount:.2f}.")