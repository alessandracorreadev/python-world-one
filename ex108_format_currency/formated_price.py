from ex108_format_currency import adjustment

price = float(input("Enter the price: $"))

print(f"Half of {adjustment.formatted(price)} is {adjustment.half(price)}")
print(f"Doble {adjustment.formatted(price)} is {adjustment.doble(price)}")
print(f"{adjustment.formatted(price)} with a 10% increase equals {adjustment.increase(price, 10)}")
print(f"{adjustment.formatted(price)} with a 10% decrease equals {adjustment.decrease(price, 10):}")