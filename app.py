import sympy as smp
import numpy as np
import operations as op

functions = {
    '+': op.add,
    '-': op.subtract,
    '*': op.multiply,
    '/': op.divide
    }

#define the values of the expression
numbers = []

def evalOperation(numbers, oper):
    fn = functions[oper]
    if len(numbers) % 2 == 0:
        a = numbers[0]
        b = numbers[1]
        solution = fn(a,b)
    return solution



def main():
    response = input("Would you like to calculate? (Y/N): ").strip().lower()
    if response == 'n':
        print("Okay, Goodbye!")
    elif response == 'y':
        expression = input("Please enter your expression (example:\"2 + 5\" ): ")
        #parse string and find characters +, /, x, -
        for letter in expression:
            #instanstiate the first number of the expression 
            if op.is_number(letter):
                numbers.append(float(letter))
            #map given string operator to correct operation
            elif letter in ('+', '-', 'x', '/','*'):
                oper = letter
        
        print(evalOperation(numbers, oper))             
    else:
        expression = input("Please enter your expression (example:\"2 + 5\" ): ")


if __name__ == "__main__":
    main()