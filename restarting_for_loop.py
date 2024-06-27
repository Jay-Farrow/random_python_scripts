# This program showcases restarting a for loop using a while loop.
# The for loop is not able to restart itself. In this case, we need 
# the help of a while loop to restart a for loop in python. The while
# loop will be executed as an outer loop and the for loop as an inner loop. 

while True:
    for i in range(1, 6):
        print(f"Current iteration: {i}")
        
        user_input = input(" Continue the inner loop? (yes/no): ")
        
        if user_input.lower() == 'no':
            print("Exit inner loop.")
            break
        elif user_input.lower() == 'yes':
            print("continue inner loop.")
        else:
            print("Invalid input.")
            continue
    
    user_input = input("Continue the outer loop? (yes/no): ")
    
    if user_input.lower() == 'no':
        print("Exit the outer loop.")
        break
    elif user_input.lower() == 'yes':
        print("Continue the outer loop.")
    else:
        print("Invalid input.")
        continue

# If we fail to set the proper logic for restarting a loop, our code can be set as an infinite loop.
# This is the first limitation of using methods to restart a loop. In some cases, the condition
# never becomes false, or if there is no chance to exit the loop code, then the code will continue.
# This situation will lead to hanging up or becoming unresponsive. 

# The other limitation is complexity. The logic and code both become complex. The logic of nested 
# loops is very tricky and complex to handle sometimes. In this situation, if we fail to set a logic
# for restarting loop, then the complexity of the program increases. This will produce undesirable output. 