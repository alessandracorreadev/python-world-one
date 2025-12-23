price = float(input("Enter the product price: $"))

price_with_discounts = price - (price * 0.05)

print(f"The product that orinally cost ${price:.2f}, with a 5% discount, will cost ${price_with_discounts:.2f}.")
