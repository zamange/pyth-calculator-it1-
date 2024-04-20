# unnittests, add, sub, mult, div, main loop, ui


def add(x, y):
    sum = x + y
    print(sum)
    return sum



def subtract(x, y):
    result = x - y
    print (result)
    return result



def multiply(x, y):
    try:
        product = x * y
    except TypeError:
        return "TypeError"
    
    return product