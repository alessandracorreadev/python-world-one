print(f"{"STORE":=^30}")

price = float(input("Enter the purchase total price: $"))

print('''Payment Methods
[1] Cash-cheque (on-time).
[2] Card (on-time).
[3] 2 installments on card.
[4] 3 or more installments on card.''')

choice = int(input("Choose the desired option: "))
total_price = 0
installment_amount = 0
installments = 0

if choice > 0 and choice <= 4:
    if choice == 1:
        total_price = price - (price * 0.1)
    elif choice == 2:
        total_price = price - (price * 0.05)
    elif choice == 3:
        installment_amount = price / 2
        total_price = price
        print(f"Your purchase will be paid in 2 installments of ${installment_amount:.2f} with no interest.")
    elif choice == 4:
        installments = int(input("Enter the number of installments: "))
        total_price = price + (price * 0.2)
        installment_amount = total_price / installments
        print(f"Your purchase will be paid in {installments} installments of ${installment_amount:.2f} with interest.")
    print(f"Your ${price:.2f} purchase will cost ${total_price:.2f} in total.")
else:
    print("Invalid option.")

