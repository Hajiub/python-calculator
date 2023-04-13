from typing import Union

Number = Union[int, float]

def addition(num1:Number, num2:Number) -> Number:
    """ Returns the sum of two numbers"""
    return num1 + num2


def subtraction(num1:Number, num2:Number) -> Number:
    """ Returns the difference between two numbers """
    return num1 - num2


def multiplication(num1:Number, num2:Number) -> Number:
    """ Returns the product of two numbers """
    return num1 * num2


def division(num1:Number, num2:Number) ->Number:
     """Returns the quotient of two numbers. Raises ZeroDivisionError if num2 is zero."""
     if num2 != 0:
         return num1 / num2
     raise ZeroDivisionError("Cannot divide by zero")


def power(num1:Number, num2:Number) -> Number:
    """Returns num1 raised to the power of num2."""
    return num1 ** num2


def prompt(text:str) -> int:
    """Prompt the user to enter a number."""
    while True:
        try:
            return int(input(text))
        except ValueError:
            pass

def prompt_symbol(text:str) -> str:
    """Prompt the user to enter a symbol (+, -, *, /, ^)."""
    while True:
        symbol = input(text)
        if symbol in ["+", "-", "*", "/", "^"]:
            return symbol

def main():
    num1   = prompt("Enter first number: ")
    num2   = prompt("Enter second number: ")
    symbol = prompt_symbol("Enter operation (+, -, *, /, ^): ")
    result = None
    match symbol:
        case "+":
            result = addition(num1, num2)
        case "-":
            result = subtraction(num1, num2)
        case "*":
            result = multiplication(num1, num2)
        case "/":
            result = division(num1, num2)
        case "^":
            result = power(num1, num2)
        case _:
            result = "Unkown input,"
    print("{} {} = {}".format(num1, num2, result))



if __name__ == "__main__":
    main()