name = str(input("Enter the player's name: "))

player = {
    "name": name,
    "goals": [],
    "total": 0
}
goals = list()

for game in range(1, 6):
    player['goals'].append(int(input(f"How many goals were scored in game {game}: ")))
player['total'] = sum(player['goals'])

print("-"*60)
print(player)
print("-"*60)

for data in player.items():
    print(f"The {data[0]} field has a value of {data[1]}.")

print("-"*60)

print(f"The player {player['name']} played in {len(player['goals'])} matches.")

for match, goal in enumerate(player['goals']):
    print(f"   => In match {match+1}, he scored {goal} goals.")
print(f"He scored a total of {player['total']} goals.")

print("-"*60)