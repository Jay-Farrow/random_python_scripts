# Task: Write a program that tests the compatibility between two people. 
# To work out the love score between two people: 
# Take both people's name and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word love occurs.
# Then combine these numbers to make a 2 digit number.
# For love scores less than 10 or greater than 90, the message should be
# "Your score is x, you go together like coke and mentos"
# For love scores between 40 and 50, the message should be:
# "Your scores is y, you are alright together."
# Otherwise, the message will just be their score:
# "Your score is z. 


print("Welcome to the love calculator!")
# Receive the input of the two names from the user. Then use the lower function to convert the string to lower case. 
name1 = str.lower(input("Please enter name one: "))
name2 = str.lower(input("Please enter name two: "))

true_count = name1.count("t")
true_count += name1.count("r")
true_count += name1.count("u")
true_count += name1.count("e")

love_count = name1.count("l")
love_count += name1.count("o")
love_count += name1.count("v")
love_count += name1.count("e")

true_count += name2.count("t")
true_count += name2.count("r")
true_count += name2.count("u")
true_count += name2.count("e")

love_count += name2.count("l")
love_count += name2.count("o")
love_count += name2.count("v")
love_count += name2.count("e") 

love_score = int(str(true_count) + str(love_count))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
if love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
if (love_score >= 10 and love_score < 40) or (love_score > 50 and love_score <= 90):
    print(f"Your score is {love_score}.")