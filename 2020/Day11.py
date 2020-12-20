import numpy as np
with open('AdventOfCode/2020/Input/Test11.txt', 'r') as Input:
    lines = [list(col) for col in Input.read().splitlines()]
matrix = np.array(lines)
# %% Part-1 and Part-2
def Calculate(part):
    mat = matrix.copy()
    Cmat = matrix.copy()
    cVal = 4
    if(part == 2):
        cVal = 5
    allSeats = matrix.size
    unchangedSeats = 0
    while (unchangedSeats != allSeats):
        mat, unchangedSeats, occupiedSeats = CountSeats(mat, Cmat, cVal)
        Cmat = mat.copy()
    return occupiedSeats


def CountSeats(mat, Cmat, cVal):
    countForSeats = 0
    countForChange = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if(mat[i][j] != '.'):
                mat[i][j], check = ChangeSeatState(i, j, mat[i][j], Cmat, cVal)
            if(not check):
                countForChange += 1
            if(mat[i][j] == '#'):
                countForSeats += 1
    return mat, countForChange, countForSeats


def ChangeSeatState(r, c, cell, Cmat, cVal):
    if(cell == 'L') and (CountAdjasentSeats(r, c, cell, Cmat)[0] == 0):
        return '#', True
    if(cell == '#') and (CountAdjasentSeats(r, c, cell, Cmat)[0] >= cVal):
        return 'L', True
    return cell, False


def CountAdjasentSeats(i, j, cell, Cmat):
    adjasentList = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1),
                    (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
    rMax = len(Cmat)
    cMax = len(Cmat[0])
    actualList = [(r, c) for r, c in adjasentList if (c > -1) and (c < cMax) and (r > -1) and (r < rMax)]
    return sum(1 for r, c in actualList if Cmat[r][c] == '#'), actualList

# %% Main
print("Part-1: a number if seats end up occupied is :", Calculate(1))
print("Part-2: a number if seats end up occupied is :", Calculate(2))
