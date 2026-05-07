def formatted_string(sentence):
    lenght = len(sentence) + 4
    print('~' * lenght)
    print(f'{sentence}'.center(lenght))
    print('~' * lenght)

formatted_string('Hi, i am:')
formatted_string('Alessandra Correa')
formatted_string('I am learning Python because I love it! <3')

