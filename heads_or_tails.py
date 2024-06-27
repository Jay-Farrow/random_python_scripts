# Task: Create a python program that simulates a coin flip. 
# We need to import the random module.
import random

tail_count = 0
head_count = 0

for i in range(0, 1000001):
    coin = random.randint(0,1)
    if coin == 0:
        tail_count += 1
    elif coin == 1:
        head_count += 1
print(f"Head count: {head_count}. Tail count: {tail_count}.")    