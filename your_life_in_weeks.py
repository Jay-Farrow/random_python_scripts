# Task: Create a program using maths and f-strings that tells us how many days, weeks, months
# we have left if we live until 90 years old. It will take your current age as the input and 
# output a message with our time left in this format: You have x days, y weeks and z months left. 
# Where x, y and z are replaced with the actual calculated numbers. 

age = int(input("What is your current age? "))

number_of_days_in_year = 365
number_of_weeks_in_year = 52
number_of_months_in_year = 12

years_left = 90 - age

days_left = years_left * number_of_days_in_year
weeks_left = years_left * number_of_weeks_in_year
months_left = years_left * number_of_months_in_year

time_left = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
print(time_left) 