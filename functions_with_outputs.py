# Functions with outputs
# The return keyword is important for returning an output from the function. the return instructs the computer that this is the end of the return. 

def format_name(first_name, last_name):
    formated_first_name = first_name.title()
    formated_last_name = last_name.title()
    
    return f"{formated_first_name} {formated_last_name}"

formated_string = format_name('JASOn', 'FaRrow')
print(formated_string)

# This function simulates the len() function. 
def length(string):
    count = 0
    for letter in string:
        count +=1
    return count

string = 'hello world! What is the weather like today?'
print(length(string))

# Multiple return values
def format_name_two(f_name, l_name):
    """Take a first and last name and format is to return the title case version of the name.""" # This is a docstring.
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name_two(input("What is your first name?"), input("What is your last name?")))


# Docstrings

# Docstrings are basically a way for us to create little bits of documentations as we're coding along in our functions
# or in our other blocks of code. Docstrings consist of three quotation marks and sit one line below a function.

# print vs return

# 