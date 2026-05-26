from ex107_price_module import adjustment

price = float(input("Enter the price: $"))

print(f"Half of ${price:.2f} is ${adjustment.half(price):.2f}")
print(f"Doble ${price:.2f} is ${adjustment.doble(price):.2f}")
print(f"${price:.2f} with a 10% increase equals ${adjustment.increase(price, 10):.2f}")
print(f"${price:.2f} with a 10% decrease equals ${adjustment.decrease(price, 10):.2f}")