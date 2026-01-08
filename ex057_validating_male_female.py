sex = input("Enter your sex (male/female): ").strip().lower()[0]

while sex not in 'FfMm':
    sex = input("Invalid data. Please, enter your sex (male/female): ").strip().lower()[0]

print(f"{sex.capitalize()} sex registered successfully.")
