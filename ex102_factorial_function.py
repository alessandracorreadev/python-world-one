def factorial(number, show=False):
    """
    -> calculates the factorial of a number.

    :param number: number to calculate the factorial
    :param show: (optional) shows or hides the factorial operation
    :return:
    """
    print('-'*60)
    counter = number
    result = 1
    while counter > 0:
        if show == True:
            if counter == 1:
                print(f"{number} =", end=' ')
            else:
                print(f"{number} x", end=' ')
        counter -= 1
        result *= number
        number -= 1
    print(result)

factorial(5, True)
factorial(5)
factorial(8, True)
help(factorial)