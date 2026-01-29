person = list()
people = list()

while True:
    # read the name and weight and add in the temporary list
    person.append(input("Enter the name: "))
    person.append(int(input("Enter the weight: ")))
    # add a copy in the right list
    people.append(person[:])
    # clear the temporary list
    person.clear()
    # ask for continue
    new_person = ' '
    # do not accept anything but Y/N
    while new_person not in 'YyNn':
        new_person = input("Do you want to continue? [Y/N]: ").strip().lower()[0]
    if new_person in 'Nn':
        break

highest_w = lowest_w = people[0][1]

for each_person in people:
    if each_person[1] > highest_w:
        highest_w = each_person[1]
    if each_person[1] < lowest_w:
        lowest_w = each_person[1]

print(f"A total of {len(people)} people were registered.")

print(f"Highest weight: {highest_w} - ", end=' ')
for weight in people:
    if weight[1] == highest_w:
        print(weight[0], end=' ')

print()

print(f"Lowest weight: {lowest_w} - ", end=' ')
for weight in people:
    if weight[1] == lowest_w:
        print(weight[0], end=' ')
