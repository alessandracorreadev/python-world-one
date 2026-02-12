matrix = [[], [], []]
even_sum = 0
col_3_sum = 0
highest_2_row = 0

for row in range(0, 3):
    for col in range(0, 3):
        number = int(input(f"Enter the value for [{row}, {col}]: "))
        matrix[row].append(number)
        if number % 2 == 0:
            even_sum += number
        if col == 2:
            col_3_sum += number
        if row == 1:
            if col == 0:
                highest_2_row = number
            else:
                if number > highest_2_row:
                    highest_2_row = number


for r in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[r][c]:^5}]', end='')
    print()

print(f"The sum of the even numbers is {even_sum}.")
print(f"The sum of the values in the third column is {col_3_sum}.")
print(f"The highest value of the second row is {highest_2_row}.")
