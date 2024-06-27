# This program showcases how to restart a while loop in Python.
# The while loop can restart without the help of other loops in python.
# Some conditional statements will help you restart the loop. These statements are if, else, elif.
# Break and continue are also used to manage the flow of a loop.

while True:
    restart_loop = False
    
    user_input = input("want to continue? (yes/no): ")
    
    if user_input.lower() == 'no':
        print("Exit the loop.")
        break
    
    elif user_input.lower() == 'yes':
        print("Continue the loop.")
        restart_loop = True
    else: 
        print("Invalid input.")
        restart_loop = True
    
    if restart_loop:
        continue