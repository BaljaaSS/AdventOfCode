from collections import Counter
lines = open('AdventOfCode/2020/Input/Test13.txt', 'r').read().splitlines()
timestamp = int(lines[0])
pattern = lines[1].split(',')
buses = [ int(bus) for bus in pattern if bus != 'x']
# %% Part-1
def GetTimeList(time):
    divMod = [divmod(time,bus) for bus in buses]
    Times = [b*(dm[0]+1) for b,dm in zip(buses, divMod)]
    iZeroMod = [divMod.index(dm) for dm in divMod if dm[1]==0]
    for i in iZeroMod:
        Times[i] = buses[i]*divMod[i][0]
    return Times

def computeMulti(time):
    Times = GetTimeList(time)
    minTime = min([t- time for t in Times])
    index = Times.index(min(Times))
    return buses[index]*minTime
# %% Part-2
def ComputePattern(tStamp):
    patternList = []
    for i in pattern:
        if(i != 'x'):
            patternList.append(tStamp)
        tStamp += 1
    return patternList

def FindTimestamp():
    pattern = ComputePattern(0)
    step = buses[0]
    tStamp = 0
    while sum(divmod(p,b)[1] for b,p in zip(buses, [p+tStamp for p in pattern])) != 0:
        tStamp += step
    return tStamp
# %% Main
print("Part-1: BusID x minTime = :", computeMulti(timestamp))
print("Part-2: Earliest timestamp is :", FindTimestamp())