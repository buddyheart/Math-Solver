import sympy as smp
import numpy as np
import operations as op

functions = {
    '+': op.add,
    '-': op.subtract,
    '*': op.multiply,
    '/': op.divide,
    'x': op.multiply
    }

def evalOperation(mainNums, oper):
    fn = functions[oper]
    if len(mainNums) % 2 == 0:
        a = mainNums[0]
        b = mainNums[1]
        solution = fn(a,b)
    return solution


mainNums = []

def main():
    response = input("Would you like to calculate? (Y/N): ").strip().lower()
    if response == 'n':
        print("Okay, Goodbye!")
    elif response == 'y':
        expression = input("Please enter your expression (example: \" 2 + 5 \" ): ").replace(' ','')
        exp = [letter for letter in expression]
        #loop to separate values in expression without operator
        for ele in range(len(exp)):
            if exp[ele] in ('+', '-', 'x', '/','*'):
                oper = exp[ele]
                mainNums.append(exp[:ele])
                mainNums.append(exp[ele+1:])
            
        #join strings together 
        for ele in range(len(mainNums)):
            mainNums[ele] = ''.join(mainNums[ele])
            mainNums[ele] = int(mainNums[ele])

        print(evalOperation(mainNums, oper))             

    else:
        expression = input("Please enter your expression (example:\" 2 + 5 \" ): ")


if __name__ == "__main__":
    main()