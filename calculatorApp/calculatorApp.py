from art import logo
import os

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    """Perform calculations based on user's choice of operation symbol"""
    print(logo)
    num1 = float(input("What's the first Number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick a operation: ")
        num2 = float(input("What's the next number?: "))
        # from user input symbol-key, get corresponding value to call a function to perform calculation
        calculations = operations[operation_symbol]
        answer = calculations(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # ask in user wants to continue calculation with current answer
        option = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if option == "y":
            num1 = answer
        else:
            should_continue = False
            # Clear terminal
            clear()
            calculator()

calculator()
