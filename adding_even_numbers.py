# Task: Write a program that calculates the sum of all even numbers from 1 to x.
# We can do this using the range function.

print("Enter a target number to sum all the even numbers up to such target number: ")
x = int(input())
total = 0


def add_even_numbers(x, total):
    for number in range(2, x + 1, 2):
        print(number)
        total += number
    return total


sum_of_all_evens = add_even_numbers(x=x, total=total)
print(sum_of_all_evens)
