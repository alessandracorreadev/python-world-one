from random import randint
from random import sample

all_sets = []
temporary_set = []

guesses = int(input("Enter the number of sets you want: "))

for sets in range(0, guesses):
    for guess in range(0, 6):
        temporary_set.append(sample(range(1, 61), 6))