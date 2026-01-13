from datetime import date

today = date.today().year
count_legal_age = 0
not_legal_age = 0

for people in range(1, 8):
    birth_year = int(input(f"Enter the birth year of person {people}: "))
    age = today - birth_year
    if age >= 21:
        count_legal_age +=1
    else:
        not_legal_age += 1

print(f"In total, we had {count_legal_age} people of legal age and {not_legal_age} minors.")