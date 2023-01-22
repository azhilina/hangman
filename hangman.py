import random
correct_word = random.choice(['python', 'java', 'swift', 'javascript'])

print("""H A N G M A N
Guess the word: """)
word = input()
if (word == correct_word):
    print('You survived!')
else:
    print('You lost!')
