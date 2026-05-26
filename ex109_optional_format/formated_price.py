from ex109_optional_format import adjustment

price = float(input("Enter the price: $"))

print(f"Half of {adjustment.formatted_c(price)} is {adjustment.half(price, True)}")
print(f"Doble {adjustment.formatted_c(price)} is {adjustment.doble(price, True)}")
print(f"{adjustment.formatted_c(price)} with a 10% increase equals {adjustment.increase(price, 10)}")
print(f"{adjustment.formatted_c(price)} with a 10% decrease equals {adjustment.decrease(price, 10):}")