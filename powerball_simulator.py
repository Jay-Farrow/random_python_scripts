# This python file simulates numbers for the powerball. User enters the number of drawings.
# Outputs the results of the drawings. Powerball number is the last number in the list. 
import random

print("Enter the number of powerball drawings:")
x = (int(input()) + 1)
print(" ")

for i in range(1,x):
    powerball_list = []
    print("Powerball Drawing:", i)
    for i in range(1,6):
        powerball_list.append(random.randrange(1,70))
    for i in range(0,1):
        powerball_list.append(random.randrange(1,27))

    print(powerball_list, "Powerball:", powerball_list[5])
    print(" ")