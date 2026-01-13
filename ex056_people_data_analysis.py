sum_age = 0
count = 0
oldest_man = ''
age_oldest_man = 0
woman_under_20 = 0

for people in range(1, 5):
    name = input(f"Enter the name of person {people}: ").strip().capitalize()
    age = int(input(f"Enter the age of person {people}: "))
    sex = input(f"Enter the sex of person {people}: (male/female) ").strip().lower()[0]
    print('-'*50)
    # adding the ages
    sum_age += age
    count += 1
    # the oldest man
    if sex in 'Mm':
        if people == 1:
            oldest_man = name
            age_oldest_man = age
        else:
            if age > age_oldest_man:
                age_oldest_man = age
                oldest_man = name
    # women under 20
    if sex in 'Ff' and age < 20:
        woman_under_20 += 1

age_average = sum_age/count

# outputs
print(f"The average age of this group is {age_average:.0f}.")
print(f"The name of the oldest man is {oldest_man} and his age is {age_oldest_man}.")

if woman_under_20 == 1:
    print(f"In this group, 1 woman is under 20 years old.")
else:
    print(f"In this group, {woman_under_20} woman are under 20 years old.")
