from random import randint
from time import sleep

numbers = list()

def sum_even(numbers_list):
    even_sum = 0
    for number in numbers_list:
        if number % 2 == 0:
            even_sum += number
    print(f"The sum of the even numbers in {numbers_list} is {even_sum}.")

def randomly():
    numbers.clear()
    print(f"Generating a list of 5 random numbers:", end=' ')
    for counter in range(0, 5):
        numb = randint(1, 10)
        numbers.append(numb)
        print(numb, end=' ')
        sleep(0.7)
    print('END!')
    sum_even(numbers)
    print("-"*60)


randomly()
randomly()
randomly()
