# Task: Create a higher lower game that compares individuals with more instagram followers. 
# For example Does Neymar have more instagram followers than Ronaldo, Higher or Lower. 

import random
import os
from art import logo
from art import vs
from game_data import data

def clear():
    os.system('cls')

print(logo)

game_start = True
while game_start:
    user_choice = input("Do you want to play higher lower game? Type 'yes' or 'no'. ").lower()
    clear()
    print(logo)
    user_score = 0
    a_dict = random.randint(0, 49)
    b_dict = random.randint(0, 49)
    if user_choice == 'yes':
        game_continues = True
        while game_continues:
            print(f"Compare A: {data[a_dict]['name']}, a {data[a_dict]['description']}, from {data[a_dict]['country']}.")   # Display information about the two comparisons.
            print(vs)
            print(f"Compare B: {data[b_dict]['name']}, a {data[b_dict]['description']}, from {data[b_dict]['country']}.")
            a_followers = data[a_dict]['follower_count']
            b_followers = data[b_dict]['follower_count']
            user_input = input("Who has more followers? Type 'A' or 'B': ").upper()    # Ask the user who has more followers.
            if user_input == 'A':
                if a_followers > b_followers:
                    clear()
                    user_score += 1
                    print(logo)
                    print(f"Correct! Current Score: {user_score}.")
                    b_dict = random.randint(0, 49)
                    while a_dict == b_dict:
                        b_dict = random.randint(0, 49)
                else:
                    print(f"Game Over! Your final score is {user_score}.")
                    game_continues = False
            elif user_input == 'B':
                if b_followers > a_followers:
                    clear()
                    print(logo)
                    user_score += 1
                    print(f"Correct! Current Score: {user_score}.")
                    a_dict = b_dict
                    b_dict = random.randint(0, 49)
                    while a_dict == b_dict:
                        b_dict = random.randint(0, 49)
                else:
                    print(f"Game Over! Your final score is {user_score}.")
                    game_continues = False
    elif user_choice == 'no':
        clear()
        print("Exited Game.")
        game_start = False

