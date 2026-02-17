from random import randint
from random import sample
from time import sleep

all_sets = []

guesses = int(input("Enter the number of sets you want: "))

for sets in range(0, guesses):
    all_sets.append(sorted(sample(range(0, 61), 6)))

print('-=' * 5, f"GENERATING {guesses} LOTTERY TICKETS", '=-' * 5)
for ticket, each_set in enumerate(all_sets):
    print(f"Ticket {ticket+1}: {each_set}")
    sleep(1)
print('-=' * 9, "GOOD LUCK!", '=-' * 9)