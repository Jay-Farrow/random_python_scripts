# Task: Write a program that works out whether if a given year is a leap year. 
# A normal year has 365 days, leap years have 366, with an extra day in february. 
# We determine whether a particular year is a leap year by on every year that is evenly
# divisbile by 4, except every year that is evenly divisible by 100, unless the year is
# also divisible by 400.

year = int(input("Please enter a year to determine if its a leap year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Is a leap year.")
        else:
            print("Not a leap year.")
    else:
        print("Is a leap year.")
else:
    print("Not a leap year.")