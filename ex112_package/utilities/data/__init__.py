def read_price(command):
    while True:
        price = input(command).strip()
        if price.replace(',', '', 1).isnumeric() or price.replace('.', '', 1).isnumeric():
            break
        else:
            print(f"ERROR: {price} is not valid.")
    if price.count(',') > 0:
        return float(price.replace(',', '.'))
    else:
        return float(price)



# teacher's solution
def read_test(msg):
    is_valid = False
    while not is_valid:
        userinput = input(msg).replace(',', '.').strip()
        if userinput.isalpha() or userinput == "":
            print(f"Error: {userinput} is INVALID.")
        else:
            is_valid = True
            return float(userinput)