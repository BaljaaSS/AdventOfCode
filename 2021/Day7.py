# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 09:40:41 2021

@author: b.sereeter
"""

Numbers = [ int(i) for i in open('Inputs/Day7T.txt', 'r').read().split(',')]

# %% Part1 and Part2 
def ComputeSumUntilN(n):
    return int(n*(n+1)/2)

def FindTotalFuelCost(numbers, part):
    maxN = max(numbers)    
    dicForSum = {}
    listOfSum = []
    for i in range(0,maxN):
        if part == 1:
            totalCost = sum([abs(j-i) for j in Numbers])
        if part ==2:
            totalCost = sum([ComputeSumUntilN(abs(j-i)) for j in Numbers])
        dicForSum[totalCost] = i 
        listOfSum.append(totalCost) 
    minCost = min(listOfSum)
    return minCost, dicForSum[minCost]

print("Part-1: total fuel cost is :", FindTotalFuelCost(Numbers.copy(),1))
print("Part-2: total fuel cost is :", FindTotalFuelCost(Numbers.copy(),2))
    