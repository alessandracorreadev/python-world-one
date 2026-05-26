# jogos = [[10, 20], [5, 50], [30, 1]]

# sum_order = sorted(jogos, key=sum)

# print(sum_order)

while True:
    print("MENU".center(50))
    valid_options = [1, 2, 3]
    user_opt = 0
    while user_opt not in valid_options:
        try:
            user_opt = int(input("Enter your option: "))
        except (ValueError, TypeError):
            print("Error: enter a valid integer nunber.")
    if user_opt == 3:
        break

    print('=' * 50)
    print(f"OPTION {user_opt}".center(50))
    print('=' * 50)