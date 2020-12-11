import operator
file1 = open('AdventOfCode/2020/Input/Input8.txt', 'r')
Lines = file1.read().splitlines()
ops = {"+": operator.add, "-": operator.sub}

# %% Part-1
def ExecuteInstruction(line, index, accumulator):
    if(line[0:3] == 'nop'):
        index += 1
    if(line[0:3] == 'acc'):
        accumulator = ops[line[4:5]](accumulator, int(line[5:]))
        index += 1
    if(line[0:3] == 'jmp'):
        index = ops[line[4:5]](index, int(line[5:]))
    return index, accumulator


def TerminateCode(lines):
    listOfVisits = [0] * len(lines)
    index = 0
    accumulator = 0
    terminated = False
    while(index < len(lines)):
        if (listOfVisits[index] >= 1):
            terminated = True
            break
        listOfVisits[index] += 1
        newIndex, accumulator = ExecuteInstruction(
            lines[index], index, accumulator)
        index = newIndex
    return accumulator, terminated
# %% Part-2
def FinishCode():
    for line in Lines:
        index = Lines.index(line)
        slines = Lines[:]
        if(line[0:3] == 'nop'):
            slines[index] = line.replace('nop', 'jmp')
        if(line[0:3] == 'jmp'):
            slines[index] = line.replace('jmp', 'nop')
        accumulator, terminated = TerminateCode(slines)
        if(not terminated):
            break
    return accumulator


# %% Main
print("Part-1: A value in the accumulator is :", TerminateCode(Lines)[0])
print("Part-2: A value in the accumulator is :", FinishCode())
