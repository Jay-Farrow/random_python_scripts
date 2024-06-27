# This program looks at local vs global scope. 

'''
enemies = 1  # global scope

def increase_enemies():
    enemies = 2 # local scope
    print(f"enemies inside the function: {enemies}")

increase_enemies()
print(f"enemies outside the function: {enemies}")
'''
# Local Scope 

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()

# Global Scope

player_health = 10
def drink_elixir():
    elixir_strength = 2
    print(player_health)
    
drink_elixir()

# There is no Block Scope in Python.

# Namespaces 

# Modifying Global Scope
enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# This method is bad for potential bugs and other problems

# Global Constants are variables which you define and you're never planning on changing it ever agiain. 
# the naming conventions in Python is to turn global constants into all uppercase. 

PI = 3.14159
URL = "https://www.google.com"
