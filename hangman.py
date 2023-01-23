import random
import string

correct_word = 'java'
# correct_word = random.choice(['python', 'java', 'swift', 'javascript'])
# new_hint = ''
# hint_word = ''
# guessed = ''
# attempts = 8
lost = 0
win = 0

# for i in range(len(correct_word)):
#        hint_word = hint_word + '-'

def nums (a):
    if (len(a) == 1):
        return True
    else:
        return False
        
def lower (b):
    return (b in list(string.ascii_lowercase))

print("H A N G M A N")
decision = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
print('')

while(decision != 'exit'):
    if(decision == 'play'):
        new_hint = ''
        hint_word = ''
        guessed = ''
        attempts = 8
        for i in range(len(correct_word)):
            hint_word = hint_word + '-'
        while(attempts > 0):
            print(hint_word)
            letter = input('Input a letter: ')
            check = set(hint_word)
            if(not nums(letter)):
                print('Please, input a single letter.')
                print('')
            elif(not lower(letter)):
                print('Please, enter a lowercase letter from the English alphabet.')
                print('')    
            elif('-' not in check):
                break
            elif(letter in guessed):
                print("You've already guessed this letter.")
                print('')
            elif((letter in correct_word) and (letter not in check)):
                new_hint = ''
                guessed = guessed + letter
                i = 0
                while i < len(correct_word):
                    if letter == correct_word[i]:
                        new_hint = new_hint + correct_word[i]
                        i = i + 1
                    else:
                        new_hint = new_hint + hint_word[i]
                        i = i + 1
                hint_word = new_hint
                if('-' not in set(hint_word)):
                    break
                else:
                    print('')
            elif(letter in check):
                print("You've already guessed this letter.")
                print('')
            else:
                print("That letter doesn't appear in the word.")
                print('')
                guessed = guessed + letter
                attempts = attempts - 1

        if('-' not in set(hint_word)):
            print("You guessed the word {}!".format(hint_word))
            print('You survived!')
            win = win + 1
            decision = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        else:
            print('You lost!')
            lost = lost + 1
            decision = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    elif(decision == 'results'):
        print('You won: {} times.'.format(win))
        print('You lost: {} times.'.format(lost))
        decision = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')

