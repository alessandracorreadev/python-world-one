player = dict()
all_players = list()
while True:
    print('-'*60)
    player.clear()
    player['name'] = str(input("Enter the player's name: "))
    matches = int(input(f"How many matches did {player['name']} play?: "))
    player['goals'] = list()
    for match in range(1, matches+1):
        player['goals'].append(int(input(f"   How many goals were scored in game {match}: ")))
    player['total'] = sum(player['goals'])
    all_players.append(player.copy())

    while True:
        proceed = input("Dou you want to continue? [Y/N]:").upper()
        if proceed in 'YN':
            break
        print("Error, enter only Y or N.")
    if proceed == 'N':
        break

print(f"{'id':>4} {'Name':<15}{'Goals':<25}{'Total':<6}")
print('-'*52)
for id, data in enumerate(all_players):
    print(f"{id+1:>4} {data['name'].capitalize():<15}{str(data['goals']):<25}{data['total']:<6}")
print('-'*52)

while True:
    id_player = int(input("Show data for which player? [999 to exit]: "))-1
    if id_player == 999+1:
        break
    if 0 <= id_player < len(all_players):
        print(f"Showing data for player {all_players[id_player]['name'].upper()}".center(60, '-'))
        for match, goals in enumerate(all_players[id_player]['goals']):
            print(f"   => In match {match + 1}, he scored {goals} goals.")
    else:
        print(f"There is no player with ID {id_player+1}. Enter a valid ID.")
    print('-'*60)
