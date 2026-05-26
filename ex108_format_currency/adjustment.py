def formatted(number=0, currency='$'):
    return f'{currency}{number:.2f}'.replace('.', ',')

def increase(value, add):
    result = round((value + (value * add/100)), 2)
    return formatted(result)

def decrease(value, substract):
    result = round((value - (value * substract/100)), 2)
    return formatted(result)

def doble(value):
    result = round((value * 2), 2)
    return formatted(result)

def half(value):
    result = round((value / 2), 2)
    return formatted(result)

