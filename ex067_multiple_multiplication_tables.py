while True:
    num = int(input("Enter a number to see its multiplication table: "))
    if num < 0:
        break
    print('-'*40)
    for count in range(1, 11):
        print(f"{num} x {count:2} = {num*count}")
    print('-' * 40)

print("End of the multiplication table program.")