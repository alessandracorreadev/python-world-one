matrix = [[], [], []]

for row in range(0, 3):
    for col in range(0, 3):
        number = int(input(f"Enter the value for [{row}, {col}]: "))
        matrix[row].append(number)

for c in range(0, 3):
    print(f"{matrix[c]}")

for r in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[r][c]:^5}]', end='')
    print()
