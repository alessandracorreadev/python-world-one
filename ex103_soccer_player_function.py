def player_record(player='unknown', goals=0):
    print(f"Player {player} scored {goals} goal(s) in the championship.")

player_name = input("Enter player's name: ").strip()
player_goals = input("Number of goals: ").strip()

# check if teh input is empty or if the input is not numeric
if player_goals == '' or not player_goals.isnumeric():
    # if true, assigns 0 to the variable
    player_goals = 0
else:
    # else, converts the value to an integer
    player_goals = int(player_goals)


player_record(player_name, player_goals)
player_record()
player_record(player_name)
