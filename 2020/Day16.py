Input = open('AdventOfCode/2020/Input/Input16.txt', 'r').read().splitlines()
# %% Parse To Lists
ind1 = Input.index('your ticket:')
ind2 = Input.index('nearby tickets:')

FieldsStr = Input[0:ind1-1]
FieldsNum = [(f.split()[-3], f.split()[-1]) for f in FieldsStr]
Fields = [list(range(int(f[0].split('-')[0]), int(f[0].split('-')[1])+1)) + list(range(int(f[1].split('-')[0]), int(f[1].split('-')[1])+1)) for f in FieldsNum]

MyTicket = Input[ind1+1:ind2-1][0].split(',')
MyTicket = [int(n) for n in MyTicket]

OtherTicketsStr = [n.split(',') for n in Input[ind2+1:]]
OtherTickets = []
for ticket in OtherTicketsStr:
    OtherTickets.append ([int(n) for n in ticket])

# %% Part-1
def ComputeRate():
    flatFields = [ n for field in Fields for n in field]
    errorList = [(n, OtherTickets.index(ticket)) for ticket in OtherTickets for n in ticket if n not in flatFields]
    sumRate = sum(n[0] for n in errorList)
    errorInd = [n[1] for n in errorList]
    return sumRate, errorInd

# %% Part-2
def Multiply(errorInd):
    # Remove invalid tickets
    errorInd.reverse()
    for i in errorInd:
        OtherTickets.pop(i) 

    # Find list for fields vs positions
    validTickets = list(map(list, zip(*OtherTickets)))
    fList = []
    for field in Fields:
        tList = []
        for ticket in validTickets:        
            s = sum(1 for n in ticket if n in field)
            if (s == len(ticket)):
                tList.append((Fields.index(field), validTickets.index(ticket)))
        fList.append(tList)

    # Find a list for the actual relation between fields and positions
    fList.sort(key=len) 
    aList = []
    comboList = []
    for ll in fList:
        for p in ll:
            if p[1] not in aList:
                comboList.append(p)
        aList.append(comboList[-1][1])
    
    # Sort the list for actual relation
    comboList.sort(key=lambda d: d[0])

    # Multiply values of six fields starting with departure
    multi = 1
    for n in comboList[0:6]:
        multi *= MyTicket[n[1]]

    return multi

# %% Main
sumR, errorInd = ComputeRate()
print("Part-1: scanning error rate is = :", sumR)
print("Part-2: Multiplication of values of six fields starting with departure is = :", Multiply(errorInd))