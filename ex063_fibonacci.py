print('-'*50)
print("FIBONACCI SEQUENCE".center(50))
print('-'*50)

terms = int(input("How many terms do you want to display? "))

n1 = 0
n2 = 1
n3 = 1

count = 3

print(f"{n1} → {n2} → {n3} → ", end='')

while count < terms:
    count +=1
    n1 = n2
    n2 = n3
    n3 = n1 + n2
    print(f"{n3} → ", end='')

print('END')
