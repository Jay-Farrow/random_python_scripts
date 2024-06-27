# Functions

# This is how we define a function.
def my_function():
    print("Hello World")

# This is how we call the function. 
my_function()

# Another trivial defining a function example. 
def greet():
    print("Hello there.")
    print("Welcome to 100 days of python.")
    print("Lets get started on today's lesson.")

# We call the newly created function.
greet()

# Functions with parameters. Or functions that allows for input.
def greeting(name, name1):
    print(f"Hello {name}.")
    print(f"How are you {name1}?")

greeting("Jason", "Corey") # example of positional argument. 

# Another trivial example of using parameters while defining functions. This allows for multiple parameters.  
def simple_addition(x, y):
    z = x + y
    print(z)


simple_addition(1,2)

# we pass arguments to parameters when calling functions. Parameter is the data being passed in to the function and arguments is the actual data referenced.

# Another example for defining a function with multiple parameters.
def greeting_with(name, location):
    print(f"Hello my name is {name}.")
    print(f"I am from {location}.")

greeting_with(location = 'Atlanta', name = 'Jason')  # example of keyword argument

# Positional argument - defualt way of calling functions. 
# Keyword argument - we add the parameter name and the argument we want to pass when calling the function.

# Simple Function
'''
def my_function():
    Do this
    Then do this
    Finally do this
'''

# Functions with inputs
'''
def my_function(something):
    Do this with something
    Then do this
    Finally do this
'''

# Functions with outputs
'''
def my_function():
    result = 3 * 2
    return result
'''

