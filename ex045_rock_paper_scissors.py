from random import randint

# Rules:
# Rock beats scissors
# Scissors beats paper
# Paper covers rock

print(f"{"Let's play ROCK, PAPER, SCISSORS!":^50}")
print('-'*50)

print('''Your options:
[1]Rock
[2]Paper
[3]Scissors''')

player = int(input("Make your choice: ")) - 1

computer = randint(0, 2)

options = ['rock', 'paper', 'scissors']

winner = ''

if 0 <= player < 3:
    print(f"The computer chose {options[computer]}.")
    print(f"The player chose {options[player]}.")
    print('-' * 50)

    if player == computer:
        print("The game ended in a tie!")
    else:
        # rock vs scissors, paper vs rock, scissors vs paper
        if (computer == 0 and player == 2) or (computer == 1 and player == 0) or (computer == 2 and player == 1):
            winner = 'computer'
        # rock vs paper, paper vs scissors, scissors vs rock
        elif (computer == 0 and player == 1) or (computer == 1 and player == 2) or (computer == 2 and player == 0):
            winner = 'player'
        print(f"The {winner} won!")
else:
    print("Inválid option.")

    # if computer == 0 and player == 1: #rock vs paper
    #     winner = 'player'
    # elif computer == 0 and player == 2: #rock vs scissors
    #     winner = 'computer'
    # elif computer == 1 and player == 0: #paper vs rock
    #     winner = 'computer'
    # elif computer == 1 and player == 2: #paper vs scissors
    #     winner = 'player'
    # elif computer == 2 and player == 0: #scissors vs rock
    #     winner = 'player'
    # elif computer == 2 and player == 1: #scissors vs paper
    #     winner = 'computer'
    #
    # print(f"The {winner} won!")
    # print('-'*50)

# I realized there were two ways to compare the choices: using strings or using integers.
# I decided to use integers to keep the code shorter, avoid too many if/elif statements,
# and clearly separate all the cases where the computer wins from those where the player wins.



