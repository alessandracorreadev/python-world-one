print('-'*50)
print("10 TERMS OF AN ARITHMETIC PROGRESSION".center(50))
print('-'*50)

first_term = int(input("Enter the first term: "))
common_dif = int(input("Enter the value of the common difference: "))
result = first_term
count = 1 # conta pra encerrar o loop
terms = 10 # recebe novos termos
count_terms = terms # acumula o termos


while terms != 0:
    while count <= count_terms:
        print(f"{result} → ", end='')
        result += common_dif
        count += 1
    print("PAUSE")
    terms = int(input("How many additional terms do you want to display?"))
    count_terms += terms


print(f"Arithmetic progression finished with {count_terms} terms displayed.")