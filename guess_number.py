# Task: Create a number guessing game.

import random

game_state = True
while game_state:
    user_input = input("Do you want to play the number guessing game? Type yes or no. ").lower()
    if user_input == 'yes':
        print("Welcome to the number guessing game!")
        print("I'm thinking of a number between 1 and 100.")
        difficulty = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
    
        if difficulty == 'easy':
            n = 10
        elif difficulty == 'hard':
            n = 5
    
        random_number = random.randint(0,100)
    

        for i in range(0,n):
            print(f"You have {n - i} attempts remaining to guess the number.")
            guess_number = int(input("Make a guess:"))
            if guess_number < random_number:
                print("Too low.")
            elif guess_number > random_number:
                print("Too high.")
            elif guess_number == random_number:
                print(f"Correct! The number is {random_number}, It took you {i} guesses.")
                break
    elif user_input == 'no':
        print("Exited Game.")
        game_state = False