# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 07:11:58 2021

@author: b.sereeter
"""

import pandas as pd
Commands = pd.read_csv("Inputs/Day2.csv")
Commands = Commands['Command'].str.split()

# %% Part1
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

# %% Part2
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

# %% Solution
print("Part-1: last position is :", PilotSubmarine(Commands))
print("Part-2: last position is :", PilotSubmarineWithAim(Commands))
    
    