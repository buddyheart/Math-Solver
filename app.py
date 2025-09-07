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

def is_Number(string):
    try:
        float(string)
        is_Number = True
    except:
        is_Number = False



mainNums = []

def main():
    response = input("Would you like to calculate? (Y/N): ").strip().lower()
    if response == 'n':
        print("Okay, Goodbye!")
    elif response == 'y':
        expression = input("Please enter your expression (example: \" 2 + 5 \" ): ").replace(' ','')
        exp = [letter for letter in expression]
        exp_sort = list()
        key = 0

        for ele in range(len(exp)):
            if exp[ele] in ('x', '/', '*', '+', '-') and not key:
                exp_sort.extend([''.join(exp[:ele]),exp[ele]])
                key = ele
            elif exp[ele] in ('x', '/', '*', '+', '-') and key:
                exp_sort.extend([''.join(exp[key+1:ele]),exp[ele]]) 
                key = ele     
            elif ele == len(exp)-1:
                exp_sort.append(''.join(exp[key+1:ele+1])) 

        i = 0
        while i <len(exp_sort):
            if exp_sort[i] in ('x', '/', '*'):
                oper = exp_sort[i]
                mainNums.extend([float(exp_sort[i-1]), float(exp_sort[i+1])])
                exp_sort[i-1:i+2] = [evalOperation(mainNums,oper)]
                i = 0
                mainNums.clear()
            else:
                i += 1

        i = 0
        while i <len(exp_sort):
            if exp_sort[i] in ('+','-'):
                oper = exp_sort[i]
                mainNums.extend([float(exp_sort[i-1]), float(exp_sort[i+1])])
                exp_sort[i-1:i+2] = [evalOperation(mainNums,oper)]
                i = 0
                mainNums.clear()
            else:
                i += 1

        
        print(exp_sort)


if __name__ == "__main__":
    main()