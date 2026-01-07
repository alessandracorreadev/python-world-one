sentence = input("Enter a sentence: ").strip().lower().split()

join_sentence = ''.join(sentence)
reversed_sentence = join_sentence[::-1]

print(join_sentence)
print(reversed_sentence)

if join_sentence == reversed_sentence:
    print("The sentence is a palindrome!")
else:
    print("The sentence is not a palindrome!")



