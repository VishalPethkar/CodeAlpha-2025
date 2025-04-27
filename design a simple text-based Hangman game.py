#Hangman Game 
#Design a text-based Hangman game. The program selects a random word, and the player guesses one letter at a time to uncover the word. You can set a limit on the number of incorrect guesses allowed.

import random

# List of words to choose from
word_list = ['python', 'hangman', 'challenge', 'programming', 'developer']

# Pick a random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create a display with underscores
display = ['_'] * word_length

# Set the number of allowed attempts
lives = 6

# Keep track of guessed letters
guessed_letters = []

print("Welcome to Hangman!")

# Main game loop
while lives > 0 and '_' in display:
    print(f"\nCurrent word: {' '.join(display)}")
    guess = input("Guess a letter: ").lower()

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    else:
        guessed_letters.append(guess)

    # Check if guess is correct
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
        print("Good guess!")
    else:
        lives -= 1
        print(f"Wrong guess! You have {lives} lives left.")

# End of game
if '_' not in display:
    print(f"\nCongratulations! You guessed the word: {''.join(display)}")
else:
    print(f"\nGame Over! The word was '{chosen_word}'.")


#Welcome to Hangman!

#Current word: _ _ _ _ _ _
#Guess a letter: a
#Wrong guess! You have 5 lives left.

#Current word: _ _ _ _ _ _
#Guess a letter: e
#Wrong guess! You have 4 lives left.

#Current word: _ _ _ _ _ _
#Guess a letter: g
#Wrong guess! You have 3 lives left.

#Current word: _ _ _ _ _ _
#Guess a letter: n
#Good guess!

#Current word: _ _ _ _ _ n
#Guess a letter: m
#Wrong guess! You have 2 lives left.

#Current word: _ _ _ _ _ n
#Guess a letter: h
#Good guess!

#Current word: _ _ _ h _ n
#Guess a letter: d
#Wrong guess! You have 1 lives left.

#Current word: _ _ _ h _ n
#Guess a letter: g
#You already guessed that letter.

#Current word: _ _ _ h _ n
#Guess a letter: o
#Good guess!

#Current word: _ _ _ h o n
#Guess a letter: k
#Wrong guess! You have 0 lives left.

#Game Over! The word was 'python'.