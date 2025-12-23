sentence = input("Enter a sentence: ").lower().strip()

print(f"The sentence contains {sentence.count('a')} occurrences of the letter 'a'.")
print(f"The letter 'a' appears for the first time at position {sentence.find('a')+1}.")
print(f"The letter 'a' appears for the last time at position {sentence.rfind('a')+1}.")