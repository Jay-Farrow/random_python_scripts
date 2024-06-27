# Task: Write a program that ask the user to play a number guessing game. 
# First we need to import the random module to use random.randint() function to randomly generate our correct number for the user to guess.
import random
import os

def clear():
    '''Clears the terminal screen when implemented.'''
    os.system('cls')

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# We'll make a function to set the difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS

# Choose a random number between 1 and 100 using the random module. 
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1, 100)
turns = set_difficulty()

game_start = True
while game_start:
    clear()
    user_input = input("Do you want to play the number guessing game? Type 'yes' or 'no'. ").lower()
    if user_input == 'yes':
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        answer = random.randint(1, 100)
        turns = set_difficulty()
        game_continues = True
        while game_continues:
            print(f"You have {turns} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess < answer:
                print("Too low.")
                turns -= 1
                if turns == 0:
                    print("You ran out of attempts.")
                    game_continues = False
            elif guess > answer:
                print("Too high.")
                turns -= 1
                if turns == 0:
                    print("You ran out of attempts.")
                    game_continues = False
            elif guess == answer:
                print(f"Correct! The number is {answer}.")
                game_continues = False
    elif user_input == 'no':
        print("Exited Game")
        game_start = False
