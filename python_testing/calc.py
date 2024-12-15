
def add(x, y):
    '''Add Function'''
    return x + y

def subtract(x, y):
    '''subtract function'''
    return x - y

def multiply(x, y):
    '''Multiply Function'''
    return x * y

def divide(x, y):
    '''Divide Function'''
    if y == 0:
        raise ValueError("divider cannot be negative or zero")
    return x / y 