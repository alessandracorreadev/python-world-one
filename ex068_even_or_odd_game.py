from random import randint

print('-'*40)
print("LET'S PLAY EVEN OR ODD!")
print('-'*40)

count = 0

while True:
    # player choose a number
    player_numb = int(input("Enter a number: "))
    # players choose even or odd
    player_choice = input("Even or odd? [E/O]: ").strip().lower()[0]
    # computer sort a number
    computer_numb = randint(1, 9)
    # sum of player and computer
    sum_numb = player_numb + computer_numb
    print('-' * 50)
    print(f"Computer choose {computer_numb}. The sum is equal {sum_numb}.", end='')
    # testing if sum is even or odd
    if sum_numb % 2 == 0:
        correct_choice = 'e'
        print("ITS EVEN!")
        print('-'*50)
    else:
        correct_choice = 'o'
        print("ITS ODD!")
        print('-' * 50)
    # break condition
    if player_choice != correct_choice:
        break
    else:
        print("YOU WIN!")
        print("Let's play again...")
        print('=' * 50)
        count += 1


print("YOU LOOSE.")
print('='*50)
print(f"GAME OVER. You win {count} times.")