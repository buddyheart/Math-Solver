

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

#function to check if a string is a number
def is_number(string):
    try:
        x = float(string)
        return True
    except:
        pass
