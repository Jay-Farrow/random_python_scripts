# This python file calculates the tip for a bill. 

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?"))
num_people = float(input("How many people to split the bill?"))
percentage = float(input("What percentage tip would you like to give? 10%, 12%, or 15%?"))
split_bill = bill/num_people
tip_amount = split_bill * (percentage/100)
total_bill = split_bill + tip_amount
print(f"Your total bill is: ${total_bill}")