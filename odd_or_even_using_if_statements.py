# Task: Write a program that works out whether if a given number is an odd or even number. 

number = int(input("Enter a number: "))

even_or_odd = number % 2 

if even_or_odd == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")