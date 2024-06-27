# Task: Write a program that calculates the body mass index (BMI) from a user's weight and height. 
# The BMI is a measure of someone's weight taking into account their height. The BMI is calculated
# by dividing the person's weight by the square of their height. 

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / (height ** 2)
print(int(bmi))