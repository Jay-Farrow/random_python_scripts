# This program simulates a calculator

# Addition
def add(n1, n2):
    return n1 + n2

# Subtraction
def subtract(n1, n2):
    return n1 - n2

# Multiplication
def multiply(n1, n2):
    return n1 * n2

# Division
def divide(n1, n2):
    return n1 / n2

# Operations Dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = float(input("What's the first number?: "))
    restart_loop = True    # Flag
    while restart_loop:
        for operator in operations:
            print(operator)
        operation_selection = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_selection]
        result = calculation_function(num1, num2)
        print(f"{num1} {operation_selection} {num2} = {result}")
        user_input = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, or type 'exit' to quit: ").lower()
        if user_input == 'y':
            num1 = result
        elif user_input == 'n':
            restart_loop = False    # Changing flag to exit while loop.
            calculator()            # Form of recursion.
        elif user_input == 'exit':
            restart_loop = False

calculator()