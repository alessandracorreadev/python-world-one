count = 0
over18 = 0
men = 0
women_20 = 0

while True:
    # counting people
    count += 1
    # input the age of a person
    print('-'*50)
    age = int(input(f"Enter the age of person {count}: "))
    # input the sex of a person
    sex = input(f"Enter the sex of person {count} (male/female): ").strip().lower()[0]
    print('-' * 50)
    # Notify that the person has been registered
    print(f"Person {count} registred sucessfully.")
    # check if the person is over 18 years old
    if age >= 18:
        over18 += 1
    # count how many men were registered
    if sex in 'mM':
        men += 1
    # count how many women are over 20 years old
    if sex in 'fF' and age > 20:
        women_20 += 1
    # ask if the user wants to register another person
    new_registration = input(f"Do you want to continue? [Y/N]: ").strip().lower()[0]
    # do not accept anything but Y or N
    while new_registration not in 'YyNn':
        print("Invalid option.", end=' ')
        new_registration = input(f"Do you want to continue? [Y/N]: ").strip().lower()[0]
    # break if answer is N
    if new_registration in 'Nn':
        break


print(f"You registered {count} people.")
print(f"A total of {over18} people are over 18." if over18 > 1 else f"A total of 1 person is over 18.")
print(f"A total of {men} men were registered." if men > 1 else f"A total of 1 man was registered.")
print(f"A total of {women_20} women are over 20 years old." if women_20 > 1 else f"A total of 1 woman is over 20 years "
                                                                                f"old.")


