file1 = open('AdventOfCode/2020/Input/Input5.txt', 'r') 
lines = file1.read().splitlines() 

# %% Part-1
def convertColumnToNumber(line):
    letters = list(line)
    cLower = 0
    cUpper = 8
    for letter in letters:
        if(letter == "R"):
            cLower = cLower + (cUpper-cLower)/2
        else:
            cUpper = cUpper - (cUpper-cLower)/2
    column = cLower
    return column

def convertRowToNumber(line):
    letters = list(line)
    rLower = 0
    rUpper = 128
    for letter in letters:
        if(letter == "B"):
            rLower = rLower + (rUpper-rLower)/2
        else:
            rUpper = rUpper - (rUpper-rLower)/2
    row = rLower
    return row

# %% Part-2
def findMySeat(seatIds):
    prev = seatIds[0]
    for seatId in seatIds[1:]:
        if (seatId-1 != prev) and (seatId != prev):
            return seatId -1
        prev = seatId

# %% Main
seatIds = []
for line in lines:
    row = convertRowToNumber(line[0:7])
    column = convertColumnToNumber(line[7:10])
    seatIds.append(row * 8 + column) 

print("Part-1: Maximum ID :", max(seatIds))     
seatIds.sort()
print("Part-2: My seat ID is :", findMySeat(seatIds))     


