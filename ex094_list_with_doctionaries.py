people = list()

while True:
    person = dict()

    person['name'] = input("Name: ")

    while True:
        person['sex'] = input("Sex [M/F]: ").upper()
        if person['sex'] in "MF":
            break
        print("Error, enter only M or F.")

    person['age'] = int(input("Age: "))

    people.append(person)
    #you can use peaple.append(person.copy())

    while True:
        proceed = input("Dou you want to continue? [Y/N]:").upper()
        if proceed in 'YN':
            break
        print("Error, enter only Y or N.")
    if proceed == 'N':
        break

sum_age = 0
women = list()
above_average = list()
for data in people:
    sum_age += data['age']
    if data['sex'] in "Ff":
        women.append(data['name'])
average = sum_age / len(people)

print('-'*60)
print(f'A) A total of {len(people)} people were registered.')
print(f"B) The average age of the group is {average:.0f} years")
print(f"C) The registered women were: {women}")


print("D) People above the average age:")
for p in people:
    if p['age'] > average:
        print(f"  Name:{p['name'].capitalize()}; sex: {p['sex']}; age: {p['age']}; ")
print("Finished.".center(60, '-'))