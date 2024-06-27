# Task: Write a program that will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill. 
import random

names = str(input("Enter a list of names separated by commas: "))
list_of_names = names.split(", ")
print(list_of_names)

x = len(list_of_names)
random_pick = random.randint(0, x-1)

print(list_of_names[random_pick])