# Task: Write a program that simulates a blind auction. 
# Import gavel ascii art from art.py 
from art import gavel
print(gavel)

# By importing the os we can use the .system method to create a clear function using the 'cls' or clear command in windows. 
import os
def clear():            
    os.system('cls')

# We'll create a function to determine the highest bid
def highest_bid(auction_dictionary):
    highest_bid = 0
    winner = ""
    for key in auction_dictionary:    # The for loop will loop through each key in a dictionary.
        bid_amount = auction_dictionary[key]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key
    
    print(f"The highest bid is ${highest_bid} the winner is {winner}.")
    

print("Welcome to the Silent Auction.")
auction_dictionary = {}

restart_loop = True
while restart_loop:
    restart_loop = False
    
    name = input("Enter name:\n")
    bid = int(input("Enter bid:\n$"))
    
    auction_dictionary[name] = bid
    user_input = input("\nAny other bids? (yes/no)\n").lower()
    if user_input == 'yes':
        clear()
        restart_loop = True
    elif user_input == 'no':
        break
    else:
        print("Invalid Input.")
        user_input = input("Any other bids? Type 'yes' or 'no'.\n").lower
        if user_input == 'yes':
            restart_loop = True
        elif user_input == 'no':
            break
        else:
            continue
    
    if restart_loop:
        continue

highest_bid(auction_dictionary=auction_dictionary)