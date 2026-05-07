from time import sleep
def largest_number(*numbers):
    print('-=' * 40)
    print("Analyzing the entered numbers..")
    largest = 0
    counter = 0
    for number in numbers:
        print(number, end=' ')
        sleep(0.5)
        if counter == 0:
            largest = number
        else:
            if number > largest:
                largest = number
        counter += 1
    print(f"- {len(numbers)} numbers were entered.")
    print(f"The largest number was {largest}.")




largest_number(2, 9, 4, 5, 7, 1)
largest_number(4, 7, 0)
largest_number(1, 2)
largest_number(6)
largest_number()
largest_number(-5,-1,-2,-3)
