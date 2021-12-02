# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 06:52:42 2021

@author: b.sereeter
"""

# %% Day1
def CountIncrease(data):
    # Part1
    count = 0
    previous = data[0]
    for m in data:
        if (m > previous):
            count += 1
        previous = m
    return count

def CountIncreaseBy3(data):
    # Part2
    sumOfThree = []
    for i in data.index:
        sumOfThree.append(data[i:i+3].sum())              
    return CountIncrease(sumOfThree)

# %% Day2
def PilotSubmarine(commands):
    # Part1
    cordinate = [0,0]
    for command in commands:
        if (command[0] == 'forward'):
            cordinate[0] = cordinate[0] + int(command[1])
        if (command[0] == 'down'):
            cordinate[1] = cordinate[1] + int(command[1])
        if (command[0] == 'up'):
            cordinate[1] = cordinate[1] - int(command[1])  
    return cordinate[0]*cordinate[1]

def PilotSubmarineWithAim(commands):
    # Part2    
    cordinate = [0,0]
    aim = 0
    for command in commands:
        if (command[0] == 'forward'):
            cordinate[0] = cordinate[0] + int(command[1])
            cordinate[1] = cordinate[1] + aim*int(command[1])
        if (command[0] == 'down'):
            aim = aim + int(command[1])
        if (command[0] == 'up'):
            aim = aim - int(command[1])  
    return cordinate[0]*cordinate[1]
# %% Day3
