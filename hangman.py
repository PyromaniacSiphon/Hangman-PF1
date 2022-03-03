import random
from words import words
import string
from hangman_visual import lives_visual_dict

def get_valid_word(words):
    word = random.choice(words)    #randomly chooses a word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)      #lettters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()          #what the user has guessed

    lives = 7

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        #what the current word is
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 #takes away a life if wrong
                print('the word doesnt contain this letter')

        elif user_letter in used_letters:
            print('Letter already used, try again')
        else:
            print('Invalid letter. Please try again.')

    # we will exit the while loop len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('you lost, the correct word is ', word)
    else:
        print('Good, you won ! :', word, '!!')
