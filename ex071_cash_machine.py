print('-' * 50)
print("WELLCOME TO OUR BANK".center(50))
print('-' * 50)

count1 = 0
count10 = 0
count20 = 0
count50 = 0

amount = int(input("How much would you like to withdraw: $"))

remaining = amount

while True:
    while remaining // 50 > 0:
        count50 += 1
        remaining -= 50
    if count50 > 0: print(f"A total of {count50} $50 bills.")

    while remaining // 20 > 0:
        count20 += 1
        remaining -= 20
    if count20 > 0: print(f"A total of {count20} $20 bills.")

    while remaining // 10 > 0:
        count10 += 1
        remaining -= 10
    if count10 > 0: print(f"A total of {count10} $10 bills.")

    while remaining // 1 > 0:
        count1 += 1
        remaining -= 1
    if count1 > 0: print(f"A total of {count1} $1 bills.")

    if remaining == 0:
        break

print('-' * 50)
print("COME BACK ANYTIME".center(50))
print('-' * 50)


