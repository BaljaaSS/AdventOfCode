# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 05:55:12 2021

AoC 2021 Day 1

@author: b.sereeter
"""

import pandas as pd
import Methods as met

measurements = pd.read_csv("Inputs/Day1.csv")

print("Part-1: number of increase is :", met.CountIncrease(measurements['Data']))
print("Part-2: number of increase by 3 is :", met.CountInreaseBy3(measurements['Data']))
    
    