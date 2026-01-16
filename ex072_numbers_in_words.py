numbers_word = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
                'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
                'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')

number = int(input("Enter a number between 0 and 20: "))

while number < 0 or number > 20:
    number = int(input("Try again. Enter a number between 0 and 20: "))

print(f"You entered number {numbers_word[number]}.")
