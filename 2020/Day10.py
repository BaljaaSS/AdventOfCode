import numpy as np
from itertools import combinations
numberList = np.genfromtxt(
    "AdventOfCode/2020/Input/Test10.txt", usecols=0, usemask=False, dtype=int).tolist()
StepList = [1, 2, 3]
countList = []
# %% Part-1
def ComputeMulti():
    path = Path('0', 0, numberList[:])
    path.ComputePath()
    print(path.pos, ":", path.path + "+" + str(3))
    print("+1 :", path.countForOne, "+3 :", path.countForThree)
    return(path.countForOne * path.countForThree)

# %% Part-2
def CountWays():
    path = Path('0', 0, numberList[:])
    path.CountWays()
    return(sum(countList))

# %% Path class
class Path:
    countForOne = 0
    countForThree = 1
    countForWays = 1

    def __init__(self, path, pos, shortList):
        self.path = path
        self.pos = pos
        self.shortList = shortList

    def ComputePath(self):
        n = len(self.shortList)
        for i in range(n):
            stepBoolList = []
            for step in StepList:
                if(step + self.pos in self.shortList):
                    index = self.shortList.index(step + self.pos)
                    stepBoolList.append((step, index))

            if(stepBoolList[0][0] == 1):
                self.countForOne += 1
            if(stepBoolList[0][0] == 3):
                self.countForThree += 1

            self.path = self.path + '+' + str(stepBoolList[0][0])
            self.pos += stepBoolList[0][0]
            self.shortList.pop(stepBoolList[0][1])
        self.countForWays = 1

    def CountWays(self):
        stepBoolList = []
        if(self.pos == max(numberList)):
            countList.append(1)
        else:
            for step in StepList:
                if(step + self.pos in self.shortList):
                    index = self.shortList.index(step + self.pos)
                    stepBoolList.append((step, index))

            for step, index in stepBoolList:
                sList = self.shortList[:]
                sList.pop(index)
                path = Path(self.path + '+' + str(step),
                            self.pos + step, sList)
                path.CountWays()

# %% Main
print("Part-1: a number of 1-jolt differences multiplied by the number of 3-jolt differences is :", ComputeMulti())
print("Part-2: a total number of distinct ways is :", CountWays())
