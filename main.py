# Step 1
import random
import hangman_words

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
words = len(chosen_word)

def space(words):
    spaces = ['_'] * words
    return spaces


display = space(words)
already=[] # this list is for elements that have already been used
lose=6
while '_' in display and lose > 0:

    guess = input("Guess a letter\n").lower()
    if guess not in already:
        already.append(guess)
    else:
        print(f"YOU HAVE ALREADY GUESSED {guess} ")
        continue


    print(f"This is the list of your already guessed letters: {already}")


    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = guess
            print(display)

    if guess not in chosen_word:
        lose-=1
        print(stages[lose])
        print(display)


    print(lose)

if lose == 0:
    print("YOU HAVE LOST!!")
else:
    print("YOU HAVE WON!!!")
    print(f"YOU HAVE GUESSED THE CORRECT WORD: {''.join(display)}")





