# Task: Write a program that simulates the word guessing game hangman. 
import random

print("Welcome to the hangman game!!")

# Create our word for guessin in hangman
word_list = ["ardvark", "baboon", "camel", "master", "python", "Fish", "projects", "hangman"]
chosen_word = random.choice(word_list)

# Create an empty list called display. to display the number of letters with blanks.
display = []
length_of_word = len(chosen_word)
for number in range(length_of_word):
    display += '_'

# Asks the user to guess a letter in the chosen word.
end_of_game = False
lives = 5

while not end_of_game:
    print("Guess a letter: ")
    guess = str.lower(input())
    
# check if the guess is a correct letter in the word. Then add it to the display in the correct position
    for position in range(length_of_word):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(f"number of lives: {lives}")
