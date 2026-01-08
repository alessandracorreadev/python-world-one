from random import randint
from time import sleep

computer = randint(0, 10)
print("I'm thinking of a number between 0 and 10...")
sleep(1)
print("Try to guess what it is!")
sleep(1)
player = int(input("What's your guess? "))
count = 1

while player != computer:
    if player > computer:
        print("Too high! Try again.")
    elif player < computer:
        print("Too low! Try again.")
    player = int(input("What's your guess? "))
    count += 1

print(f"Congratulations! You got it right in {count} attempts.")

# try to use a variable called "hit" with false and true
# while not hit
# if player == computer than hit = True
