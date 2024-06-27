# Task: write a function that checks whether if the number passed into the function
# is a prime number or not. For review, a prime number is a number that can only be 
# divided by themselves and 1. For example, 2.

def prime_checker(number):
    if number == 2:
        print("Is a prime number.")

    elif number == 3:
        print("Is a prime number.")

    elif number % 2 == 0 or number % 3 == 0:
        print("Not a prime number.")

    else:
        print("Is a prime number.")

for i in range(1, 101):
    print(f"Number: {i}.")
    prime_checker(i)

