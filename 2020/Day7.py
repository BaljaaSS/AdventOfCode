from array import *
file1 = open('AdventOfCode/2020/Input/Input7.txt', 'r') 
lines = file1.read().splitlines() 

# %% Main
class Bag:
    childBags = []
    def __init__(self, color, num):
        self.color = color
        self.num = num 

    def countBag(self):
        sum = 0
        if (self.childBags[0] == None):
            return self.num

        for cbag in self.childBags:
            sum += cbag.num * FindBag(cbag.color).countBag() + cbag.num
        return sum

def ParseToBagObject(line):
    listOfBags = line.split(',')
    childList = []
    for item in listOfBags[1:]:
        bagStr = item.strip()
        if(bagStr != 'no other'):
            childList.append(Bag(bagStr[2:], int(bagStr[0:1])))
        else:    
            childList.append(None)

    bag = Bag(listOfBags[0].strip(), 1)        
    bag.childBags = childList    
    if(childList[0] == None):
        bag.num = 0    
    return bag

listOfBags = []
for line in lines:
    line = line.replace('bags contain',',').replace('bags','').replace('bag','').replace('.','').strip()
    listOfBags.append(ParseToBagObject(line))

# %% Part-1 code without OOP
def computeParentsList(oldParentList):
    newParentList = []
    for bag in oldParentList:
        for line in lines:
            line = line.replace('bags contain',',').replace('bags','').replace('bag','').replace('.','').strip()
            listOfBags = line.split(',')
            if any(bag in b for b in listOfBags[1:]) and not any(listOfBags[0].strip() in b for b in actualParentList):
                    actualParentList.append(listOfBags[0].strip())
                    newParentList.append(listOfBags[0].strip())    
    return newParentList

actualParentList = []
def computeParentBags(parentList):
    while len(parentList) != 0:
        parentList = computeParentsList(parentList)
    return len(actualParentList)  

print("Part-1: A number of bags can contain my \'shiny gold\' bag is :", computeParentBags(['shiny gold']))    

# %% Part-2 code
def FindBag(bagStr):
    for bag in listOfBags:
        if (bag.color == bagStr):
            return bag
            break   
        
def ComputeTotalBags(bagStr):
    bag = FindBag(bagStr)
    return bag.countBag()

print("Part-2: A number of total bags can fit inside my \'shiny gold\' bag is :", ComputeTotalBags('shiny gold'))    