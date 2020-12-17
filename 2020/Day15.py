Input = open('AdventOfCode/2020/Input/Input15.txt', 'r').read()
# %% Parse To Lists
numDic = {}
tNum = 1
for n in Input.split(','):
    numDic.update({int(n): [tNum, tNum]})
    tNum += 1

# %% Part-1 and Part-2
def FindLastSpokenNum(nDic, e):
    s = len(nDic) + 1
    lastNum = list(nDic.keys())[-1]
    for i in range(s,e+1):
        ldic = nDic.get(lastNum,[i,i])
        lastNum = ldic[0]-ldic[1]
        nDic.update({lastNum: [i, nDic.get(lastNum,[i,i])[0]]})

    return lastNum
# %% Main
print("Part-1: the 2020th number spoken is = :", FindLastSpokenNum(numDic.copy(), 2020))
print("Part-2: the 30000000th number spoken is = :", FindLastSpokenNum(numDic.copy(), 30000000))