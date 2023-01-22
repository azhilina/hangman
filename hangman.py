import random
correct_word = random.choice(['python', 'java', 'swift', 'javascript'])
hint_word = ''
for i in range(len(correct_word)):
    if i < 3:
        hint_word = hint_word + correct_word[i]
    else:
        hint_word = hint_word + '-'

print("""H A N G M A N
Guess the word: """, hint_word)
word = input()
if (word == correct_word):
    print('You survived!')
else:
    print('You lost!')
