from random import choice

player = int(input("Make your choice: ")) - 1

print(player)

options = ['rock', 'paper', 'scissors']

computer = choice(options)

print(computer)