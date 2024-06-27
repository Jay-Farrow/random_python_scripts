# Task: Write a password generator. The generator ask the user the password length,
# How many symbols in the passwords, and how many numbers in the password.
# By using for loops and lists we can create the password generator.
import random

# We create lists consisting of letters from the alpahbet, a list of number 0-9, and a list of symbols consisting of 9 different symbols.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Then we ask for user input for how many letters, symbols, and numbers that they want in their random password. 
print("Welcome to the PyPassword Generator")
print("How many letters would you like in your password? ")
number_of_letters = int(input())
print("How many symbols would you like? ")
number_of_symbols = int(input())
print("How many numbers would you like? ")
number_of_numbers = int(input())

# password = ''
password = []
'''
for number in range(1, number_of_letters + 1):    # We could also use random.choice(letters), which will random select an item from our list.
    n = random.randint(0, 51)
    password += letters[n]

for number in range(1, number_of_symbols + 1):
    n = random.randint(0, 8)
    password += symbols[n]

for number in range(1, number_of_numbers + 1):
    n = random.randint(0, 9)
    password += numbers[n]
'''
# Another way to accomplish the random password is using a list to store the characters
# and then using the random.shuffle() method to random sort the list of characters.

for number in range(1, number_of_letters + 1):
    n = random.choice(letters)
    password += n

for number in range(1, number_of_symbols + 1):
    n = random.choice(symbols)
    password += n
    
for number in range(1, number_of_numbers + 1):
    n = random.choice(numbers)
    password += n

random.shuffle(password)
password = "".join(password)
print(f"Generated Password: {password}")