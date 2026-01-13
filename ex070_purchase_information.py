cheapest = 0
name_cheapest = ''
more_than_1000 = 0
total = 0
count = 0

print('-'*50)
print("WELLCOME TO DEPARTMENT STORE".center(50))
print('-'*50)

while True:
    # counting products
    count += 1
    # ask name of the product
    product = input("Name of the product: ")
    # ask the price of the product
    price = float(input("Price: $"))
    # add to total purchase
    total += price
    # count how many products cost more than $1000.
    if price > 1000:
        more_than_1000 += 1
    # find the cheapest product
    if count == 1:
        cheapest = price
        name_cheapest = product
    else:
        if price < cheapest:
            cheapest = price
            name_cheapest = product
    # ask if want to continue to register products
    new_product = ' '
    while new_product not in 'yYnN':
        new_product = input("Do you want to add a new product? [Y/N]: ").strip().lower()[0]
    if new_product in 'nN':
        break

print()
print("END PROGRAM".center(50, '-'))

print(f"The total purchase amount is ${total:.2f}.")

if more_than_1000 == 0:
    print(f"No product costs more than $1000.00.")
elif more_than_1000 == 1:
    print("1 product costs more than $1000.00.")
else:
    print(f"{more_than_1000} products costs more than $1000.00.")

print(f"The cheapest product is {name_cheapest} and it costs ${cheapest:.2f}.")


# the if-else for the cheapest price can be replaced:

# if count == 1 or price < cheapest:
#     cheapest = price
#     name_cheapest = product
