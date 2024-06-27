# This python file uses a function to calculate the total price of crawfish per pound. 

def cost_of_crawfish(pound, price):
    total_cost = pound * price
    return "The Total Cost: ${:.2f}".format(total_cost)  
    
print("Enter the amount of crawfish in pounds.")
pound = int(input())

print("Enter the price of crawfish.")
price = float(input())

print(cost_of_crawfish(pound, price))