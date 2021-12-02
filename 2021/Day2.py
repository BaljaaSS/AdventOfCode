# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 07:11:58 2021

@author: b.sereeter
"""

import pandas as pd
import Methods as met

Commands = pd.read_csv("Inputs/Day2.csv")
Commands = Commands['Command'].str.split()

print("Part-1: last position is :", met.PilotSubmarine(Commands))
print("Part-2: last position is :", met.PilotSubmarineWithAim(Commands))
    
    