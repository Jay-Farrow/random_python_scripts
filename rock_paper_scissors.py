# Task: Create a rock, paper, scissors game using the random module.

import random

comp = random.randint(0, 2)

user = int(input("Type 0 for Rock, 1 for Paper, and 2 for Scissors: "))

if user == 0:
    user = 'Rock'
    print(f"You chose {user}.")
elif user == 1:
    user = 'Paper'
    print(f"You chose {user}.")
elif user == 2:
    user = 'Scissors'
    print(f"You chose {user}.")

if comp == 0:
    comp = 'Rock'
    print(f"Computer chose {comp}.")
elif comp == 1:
    comp = 'Paper'
    print(f"Computer chose {comp}.")
elif comp == 2:
    comp = 'Scissors'
    print(f"Computer chose {comp}.")

if user == 'Rock' and comp == 'Scissors':
    print("You win")
elif user == 'Rock' and comp == 'Paper':
    print("You lose")
elif user == 'Rock' and comp == 'Rock':
    print("You tied")
elif user == 'Paper' and comp == 'Scissors':
    print("You lose")
elif user == 'Paper' and comp == 'Rock':
    print("You win")
elif user == 'Paper' and comp == 'Paper':
    print("You tied")
elif user == 'Scissors' and comp == 'Paper':
    print("You win")
elif user == 'Scissors' and comp == 'Rock':
    print("You lose")
elif user == 'Scissors' and comp == 'Scissors':
    print("You tied")