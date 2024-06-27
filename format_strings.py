# This python file shows examples of using the format() method.

# Inserting numbers into strings
age = 27 
txt = "My name is Jason, and I am {}."
print(txt.format(age))

# Inserting multiple arguments into a string.
quantity = 3
itemnum = 567
price = 49.59
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemnum, price))

# Inserting multiple arguments while specifying arguments into a string. 
quantity = 3
itemnum = 567
price = 49.59
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemnum, price))

# The code displays the message Hello, Jason Farrow!
first_name = "jason"
last_name = "farrow"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)