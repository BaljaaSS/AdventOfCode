from itertools import product, permutations, combinations
import numpy as np
# %% Parse into List
Input = open('AdventOfCode/2020/Input/Input17.txt', 'r').read().splitlines()
flatRegion = [0 if cell == '.' else 1 for line in Input for cell in line]
n = len(Input)

def UpdateCord(cDic, n, dim):
    combos = list(product(list(range(n)),repeat=2))
    i=0
    for combo in combos:
        if (dim ==3):
           cDic.update({combo+ (0,): flatRegion[i]})
        else:
            cDic.update({combo+ (0,0): flatRegion[i]})
        i+=1

def FindNeighbors(cord, dim):
    cord1 = [[i-1, i, i+1] for i in cord]
    if dim ==3:
        combos = [(x,y,z) for x in cord1[0] for y in cord1[1] for z in cord1[2]]
    else:
        combos = [(x,y,z,w) for x in cord1[0] for y in cord1[1] for z in cord1[2] for w in cord1[3]]
    combos.remove(cord)    
    return combos

# %% Part-1 and Part-2
def IncludeNeighborsOfOne(cDic, dim):
    nDic = cDic.copy()
    for combo in nDic:
        if (cDic.get(combo) == 1):
            neighbors = FindNeighbors(combo,dim)
            for nb in neighbors:
                cDic.update({nb: cDic.get(nb,0)})

def DoCycle(it, s, dim):
    cordDic = {}
    UpdateCord(cordDic, n, dim)
    cDic = cordDic.copy()
    cDic1 = cDic.copy()    
    for i in range(1,7):
        IncludeNeighborsOfOne(cDic,dim)
        for combo in cDic:
            cube = cDic.get(combo,0)
            neighbors = FindNeighbors(combo,dim)
            activeCubes = sum(cDic.get(c,0) for c in neighbors)
            if cube == 1 and activeCubes not in [2, 3]:
                cDic1.update({combo: 0})
            if cube == 0 and activeCubes == 3:
                cDic1.update({combo: 1})                
        cDic = cDic1.copy()
        sumForActive = sum(cDic.get(c) for c in cDic)
        print('After cycle', i, ':', sumForActive)
    return sumForActive

# %% Main
print("Part-1: A number of active 3D cubes after the 6 cycle is = :", DoCycle(6, n, 3))
print("Part-1: A number of active 4D cubes after the 6 cycle is = :", DoCycle(6, n, 4))