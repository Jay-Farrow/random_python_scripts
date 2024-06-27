# First, convert this function is_leap() so that instead of printing 'leap year' or 'not leap year'
# it should return True if it is a leap year and False if it is not a leap year. Then create
# a new function called days_in_month() which will take a year and a month as inputs. Then the 
# function will use this information to work out if the year is a leap year and decide the number
# of days in a month, then return that as the output. 

# First we define the is_leap() function to determine if a given year is a leap year or not.
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Now, we define the days_in_month() function.
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    elif is_leap(year):
        return month_days[month - 1]
    else:
        return month_days[month - 1]

year = int(input("Enter a year:\n"))
month = int(input("Enter a month:\n"))
days = days_in_month(year, month)
print(days)