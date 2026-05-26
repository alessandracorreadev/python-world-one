def formatted_c(number=0, currency='$'):
    return f'{currency}{number:.2f}'.replace('.', ',')

def increase(value, add, formatted=False):
    result = round((value + (value * add/100)), 2)
    return formatted_c(result) if formatted else result

def decrease(value, substract,formatted=False):
    result = round((value - (value * substract/100)), 2)
    return formatted_c(result) if formatted else result

def doble(value, formatted=False):
    result = round((value * 2), 2)
    return formatted_c(result) if formatted else result

def half(value, formatted=False):
    result = round((value / 2), 2)
    return formatted_c(result) if formatted else result

def analysis(price, incr=0, decr=0):
    print('-' * 30)
    print('PRICE ANALYSIS'.center(30))
    print('-' * 30)
    print(f"{'Price analyzed:'.ljust(20)}{formatted_c(price)}")
    print(f"{'Double the price::'.ljust(20)}{doble(price, True)}")
    print(f"{'Half the price:'.ljust(20)}{half(price, True)}")
    print(f"{incr}% increase:".ljust(20) + f"{increase(price, incr, True)}")
    print(f"{decr}% reduction:".ljust(20) + f"{decrease(price, decr, True)}")
    print('-' * 30)
