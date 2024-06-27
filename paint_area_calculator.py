# Task: You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 
# 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint 
# you'll need to buy. Create a function to solve this problem. 

def paint_calc(height, width, cover):
    number_of_cans = (height*width) / cover
    print(f"You'll need {round(number_of_cans)} cans of paint.")

test_h = int(input("Enter the height of the wall: "))
test_w = int(input("Enter the width of the wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)