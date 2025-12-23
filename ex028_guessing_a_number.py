from random import randint
from time import sleep

computer = randint(0, 5)
print("I'm thinking of a number between 0 and 5...")
sleep(1)
print("Try to guess what it is!")
sleep(2)
player = int(input("What's your guess? "))

if computer == player:
    print(f"You got it right! I really was thinking of the number {computer}.")
    print("You WIN!")
else:
    print(f"Sorry, you're wrong! I was thinking of the number {computer}.")
    print("Computer WIN!")
