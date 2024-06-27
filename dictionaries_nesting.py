# Python Dictionaries

# A Python Dictionary is a set of key-value pairs. A dictionary is an object class dict.
# It's an unordered collection which means that while iterating the order of retrieval is not guaranteed.
# The key and value is separated by a colon. Dictionary records are indexed using the key. 

# The keys are unique in a dictionary. It is used to retrieve the records from the dictionary. 
# A dictionary is created by using a pair of braces. The key-value pairs are separated using a comma. 
# Dictionary keys are immutable. So we can use strings, numbers, and tuples as dict keys. 

# Dictionaries consist of key : value pairs.
programming_dictionary = {
    "Bug" : "An error in a program that prevents the program from running as expected.",
    "Function" : "A piece of code that you can easily call over and over again.",
    "Loop" : "The action of doing something over and over again.",
}

# Retrieving items from a dictionary.
print(programming_dictionary)
print(programming_dictionary["Bug"])    # We can call the value from a dictionary by its key. 

data_types_dictionary = {
    "String" : "The data type consisting of characters forming a string.",
    "Int" : "The numeric integer data type consist of whole numbers from negative infinity to infinity.",
    "Float" : "The numeric float data type consist of floating point numbers or fractional numbers.",
    "Boolean" : "The boolean data type consist two values True or False.",
}

print(data_types_dictionary["String"])

# Adding new items to dictionary.
data_types_dictionary["Sequence"] = "The sequence data types are list, tuple, and set."
print(data_types_dictionary)

# Create empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary by creating an empty dictionary. 

# We can edit an item in a dictionary by redefining its value by using its key. 
programming_dictionary["Bug"] = "New definition."
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


# Nesting list and dictionaries
# {Key: [List], Key2: {dict}}

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"],
}

# Nest a dictionary in a dictionary

travel_log_labels = {
    "France": {"Paris": "Visited: 2 times.", "Lille": "Visited: 1 time.", "Dijon": "Visited: 7 times."},
    "Germany": {"Berlin": "Visited: 3 times.", "Hamburg": "Visited: 1 time.", "Stuttgart": "Visited 3 times."},
}

print(travel_log_labels)
print(travel_log_labels["France"])
print(travel_log_labels["France"]["Paris"])


# Nesting a dictionary in a list
travel_log_list = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 13
    },
]

print(travel_log_list[1])
