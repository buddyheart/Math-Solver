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
placeHolder = [[],[]]

def main():
    response = input("Would you like to calculate? (Y/N): ").strip().lower()
    if response == 'n':
        print("Okay, Goodbye!")
    elif response == 'y':
        expression = input("Please enter your expression (example: \" 2 + 5 \" ): ").replace(' ','')
        exp = [letter for letter in expression]
        exp_sort = list()

        n = 2
        key = 0
        #L[1:3] = [''.join(L[1:3])]
        for ele in range(len(exp)):
            if exp[ele] in ('x', '/', '*', '+', '-') and not key:
                exp_sort.extend([''.join(exp[:ele]),exp[ele]])
                key = ele
            elif exp[ele] in ('x', '/', '*', '+', '-') and key:
                exp_sort.extend([''.join(exp[key+1:ele]),exp[ele]]) 
                key = ele     
            elif ele == len(exp)-1:
                exp_sort.append(''.join(exp[key+1:ele+1])) 



        print(exp_sort)            

        #loop to separate values in expression without operator
        '''
        for ele in range(len(exp)):
            if exp[ele] in ('+', '-', 'x', '/','*'):
                oper = exp[ele]
                mainNums.append(exp[:ele])
                mainNums.append(exp[ele+1:])
                print(mainNums)
        #join strings together 
        for ele in range(len(mainNums)):
            mainNums[ele] = ''.join(mainNums[ele])
            mainNums[ele] = int(mainNums[ele])

        print(evalOperation(mainNums, oper))             

    else:
        expression = input("Please enter your expression (example:\" 2 + 5 \" ): ")
    '''

if __name__ == "__main__":
    main()