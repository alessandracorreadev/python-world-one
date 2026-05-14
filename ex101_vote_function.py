from datetime import date


def vote(year):
    age = date.today().year - year
    print(f"At {age} years old: ", end='')
    if age < 16:
        return 'CANNOT VOTE.'
    elif 16 <= age < 18:
        return 'OPTIONAL VOTING.'
    else:
        return 'VOTING IS MANDATORY.'


birth_year = int(input("Enter the birth year: "))
print(vote(birth_year))