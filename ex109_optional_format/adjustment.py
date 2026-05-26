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
