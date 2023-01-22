import random
# correct_word = 'java'
correct_word = random.choice(['python', 'java', 'swift', 'javascript'])
hint_word = ''
new_hint = ''
for i in range(len(correct_word)):
        hint_word = hint_word + '-'
attempts = 8

print("H A N G M A N")
print('')
while(attempts > 0):
    print(hint_word)
    letter = input('Input a letter: ')
    check = set(hint_word)
    if('-' not in check):
        break
    elif((letter in correct_word) and (letter not in check)):
        new_hint = ''
        i = 0
        while i < len(correct_word):
            if letter == correct_word[i]:
                new_hint = new_hint + correct_word[i]
                i = i + 1
            else:
                new_hint = new_hint + hint_word[i]
                i = i + 1
        hint_word = new_hint
        print('')
        if('-' not in set(hint_word)):
            break
    elif(letter in check):
        print('No improvements.')
        print('')
        attempts = attempts - 1
    else:
        print("That letter doesn't appear in the word.")
        print('')
        attempts = attempts - 1

if('-' not in set(hint_word)):
    print(hint_word)
    print("""You guessed the word!
You survived!""")
else:
    print('You lost!')
