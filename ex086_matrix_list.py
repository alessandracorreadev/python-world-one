matrix = [[[], [], []],
          [[], [], []],
          [[], [], []]]

for row in range(0, 3):
    for col in range(0, 3):
        number = int(input(f"Enter the value for [{row}, {col}]: "))
        matrix[row][col].append(number)

for c in range(0, 3):
    print(f"{matrix[c]}")

