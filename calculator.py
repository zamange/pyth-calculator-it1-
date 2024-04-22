# unnittests, add, sub, mult, div, main loop, ui


def user_input():
    num1 = print("Enter the first number: ")
    num2 = print("Enter the second number: ")
    return num1, num2


def add(num1, num2):
    sum = num1 + num2
    print(sum)
    return sum 



def subtract(num1, num2):
    result = num1 - num2
    print (result)
    return result



def multiply(num1, num2):
    try:
        product = num1 * num2
    except TypeError:
        return "TypeError"
    
    return product
    


def divide(num1, num2):
    try:
        quotient = num1 / num2
        return quotient
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero")
    except TypeError:
        raise TypeError("Unsupported operand types")