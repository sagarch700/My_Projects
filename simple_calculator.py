from simple_calculator_logo import logo
import os

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def square(num1, num2):
    return num1 ** num2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    "**" : square
}


def calculator():

    ''' Does the Basic arithmetic operation of tow numbers.
    
    This Function simply does the basic airthmetic operation of two input numbers.

    '''
    
    print(logo)
    num1 = float(input("What is the first number?: "))
    for operation in operations:
        print(operation)
    end_calculation = False

    while not end_calculation:
        operator = input("pick an operator: ")
        num2 = float(input("what is the second number? "))
        arithmetic_function = operations[operator]
        answer = arithmetic_function(num1, num2)

        print(f"{num1} {operator} {num2} = {answer}")

        if input(f"Tye 'Y' to continue calculating with {answer}, or type 'N' to start a new calculation: ").lower() == 'y':
            num1 = answer
        else:
            end_calculation = True
            os.system('clear')
            calculator()

calculator()
