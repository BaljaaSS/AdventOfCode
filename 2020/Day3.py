file1 = open('AdventOfCode/2020/Input/Input3.txt', 'r') 
lines = file1.read().splitlines() 

slope = [(1,1),(3,1),(5,1),(7,1), (1,2)]

## Part-1 and Part-2
mult = 1
for xStep, yStep in slope:
    xIndex = 0
    yIndex = 0
    counter = 0
    while yIndex < len(lines)-1:
        xIndex += xStep
        yIndex += yStep
        line = lines[yIndex]
        y = len(line)
        if (xIndex >= len(line)):
            xIndex -= len(line)

        if (line[xIndex] == '#'):
            counter += 1

    print("A number of trees for slope (" + str(xStep) + "," + str(yStep) + ") is :", counter)
    mult *= counter

print("Total multiplied trees", mult)