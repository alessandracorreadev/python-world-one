from random import randint
from time import sleep

players_game = dict()

# print the rolled values and add to dict()
print("Rolled values:".center(30, '-'))
for player in range(1, 5):
    dice = randint(1, 6)
    players_game[f'player{player}'] = dice
    print(f"player{player} rolled: {dice}")
    sleep(1)
print("-"*30)

#print(players_game.items())


# print the ranking
print("Ranking:".center(30, '-'))

sorted_game = sorted(players_game.items(), key=lambda item: item[1])
#print(sorted_game)

for position, player in enumerate(sorted_game):
    print(f"Place {position+1}: {player[0]} with {player[1]}")
    sleep(1)

print('-'*30)

#from operator import itemgetter
#ranking = sorted(players_game.items(), key=itemgetter(1), reverse=True)