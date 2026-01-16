words = ("apple", "computer", "music", "orange", "beautiful", "house", "window", "notebook", "coffee", "language")

for word in words:
    print(f"The word {word.upper()} contains: ", end='')
    for letter in word:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')
    print()

