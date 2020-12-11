import numpy as np
from itertools import combinations
numberList = np.genfromtxt(
    "AdventOfCode/2020/Input/Input9.txt", usecols=0, usemask=False)
# %% Part-1
def FindInvalidNumber():
    firstIndex = 0
    for x in numberList[preambleLen:]:
        lastIndex = firstIndex + preambleLen
        if (not CheckSum(x, numberList[firstIndex:lastIndex])):
            return x, lastIndex
        firstIndex += 1


def CheckSum(sumVal, numberList):
    combos = combinations(numberList, 2)
    for comb in combos:
        if (sum(comb) == sumVal):
            return True
    return False

# %% Part-2
def FindWeakness(invalidNum, index):
    numList = numberList[:index].tolist()
    check = True
    lenOfCombo = 3
    while check:
        cList = CreateListofCombos(numList, lenOfCombo)
        lenOfCombo += 1
        combos = filter(lambda e: sum(e) == invalidNum, cList)
        for comb in combos:
            check = False
            return max(comb) + min(comb)


def CreateListofCombos(numList, LenOfCombo):
    comboList = []
    for i in range(len(numList)-(LenOfCombo-1)):
        comb = ()
        for j in range(i, i+LenOfCombo):
            comb += (numList[j],)
        comboList.append(comb)
    return comboList


# %% Main
preambleLen = 25
invalidNumber, index = FindInvalidNumber()
print("Part-1: A first number that does not follow the rule is :", invalidNumber)
print("Part-2: A value in the accumulator is :",
      FindWeakness(invalidNumber, index))
