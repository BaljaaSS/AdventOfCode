import operator
from numpy import prod
Input = open('AdventOfCode/2020/Input/Input18.txt', 'r')
Lines = Input.read().splitlines()
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}

# %% Part-1
def SolveExpresP1(expr,ind=0):
    i = ind
    val = expr[i]
    while i < len(expr)-1:
        if expr[i] == ')':
            return val, i

        if expr[i] == '(':
            pVal,ind = SolveExpresP1(expr, i+1)
            if(expr[i-1] =='(') or i ==0:
                val = pVal
            else:
                val = ops[expr[i]](int(expr[i-1]), int(pVal))
            i = ind

        if expr[i] in ops:
            if (expr[i+1] == '('):
                pVal,ind = SolveExpresP1(expr, i+2)
                val = ops[expr[i]](int(expr[i-1]), int(pVal))
                i = ind
            else:    
                val = ops[expr[i]](int(expr[i-1]), int(expr[i+1]))
                i += 1

        expr[i] = val
        i +=1
    return val,i

# %% Part-2
def ComputeOper(expr, i,j, pval):
    if (j >= len(expr)):
        val = ops[expr[i]](int(expr[i-1]), int(pval))
        i = j-1
    else:
        if expr[i] == "*":
            if expr[j] == ')' or expr[j] == '*':
                val = ops[expr[i]](int(expr[i-1]), int(pval))
                i = j
            else:
                pval,ind = SolveExpresP2(expr, i+1)
                val = ops[expr[i]](int(expr[i-1]), int(pval))
                if ind == len(expr):
                    ind -=1
                i = ind           
        else:
            val = ops[expr[i]](int(expr[i-1]), int(pval))
            i = j
    return val,i
def SolveExpresP2(expr,ind=0):
    i = ind
    val = expr[i]
    while i <= len(expr)-1:
        if expr[i] == ')':
            return val, i

        if expr[i] == '(':
            pVal,ind = SolveExpresP2(expr, i+1)
            if(expr[i-1] =='(') or i ==0:
                val = pVal
            else:
                val,ind = ComputeOper(expr,i,ind,pVal)
            i = ind
            if i == len(expr):
                return val, i

        if expr[i] in ops:
            if (expr[i+1] == '('):
                pVal,ind = SolveExpresP2(expr, i+2)      
                val,ind = ComputeOper(expr,i,ind, pVal)
                i = ind
            else:    
                val, ind = ComputeOper(expr,i, i+1, expr[i+1])
                i = ind                    

        expr[i] = val
        i +=1
    return val,i
# %% Main
def SumExpressions():
    sumForExpres1 = 0 
    sumForExpres2 = 0 
    for line in Lines[1:]:
        line = list(line.replace(" ", ""))
        # solution1 = SolveExpresP1(line[:])
        # sumForExpres1 += solution1[0]
        solution2 = SolveExpresP2(line[:],0)
        sumForExpres2 += solution2[0]
        print(solution2[0])
    return sumForExpres1, sumForExpres2
sumOfExp = SumExpressions()
# print("Part-1: Sum of all expressions is :", sumOfExp[0])
print("Part-2: A value in the accumulator is :", sumOfExp[1])