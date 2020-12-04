import collections

file1 = open('AdventOfCode2020/Input2.txt', 'r') 
lines = file1.read().splitlines() 

def checkIndexOfPasswords(firstIndex, secondIndex, letter, password):
    if(password[firstIndex-1] == letter) != (password[secondIndex-1] == letter):
        return True
    else:
        return False

def findNumberofCorrectPasswords(minVal, maxVal, letter, password):
    countResult = collections.Counter(password)
    if (minVal <= countResult[letter]) and (countResult[letter] <= maxVal):
        return True
    else:
        return False

countOne = 0
countTwo = 0
for line in lines: 
    x = line.split()
    minMaxVal = x[0].split("-")
    ## Part-1
    if (findNumberofCorrectPasswords(int(minMaxVal[0]), int(minMaxVal[1]), x[1].replace(":",""), x[2])):
        countOne += 1
    ## Part-2
    if (checkIndexOfPasswords(int(minMaxVal[0]), int(minMaxVal[1]), x[1].replace(":",""), x[2])    ):
        countTwo += 1    

print("Part-1: a number of correct passwords is :", countOne)
print("Part-2: a number of correct passwords is :", countTwo)

