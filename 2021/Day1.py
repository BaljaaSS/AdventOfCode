# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 05:55:12 2021

AoC 2021 Day 1

@author: b.sereeter
"""

import pandas as pd
measurements = pd.read_csv("Inputs/Day1.csv")

# %% Part1
def CountIncrease(data):
    # Part1
    count = 0
    previous = data[0]
    for m in data:
        if (m > previous):
            count += 1
        previous = m
    return count

# %% Part2
def CountIncreaseBy3(data):
    sumOfThree = []
    for i in data.index:
        sumOfThree.append(data[i:i+3].sum())              
    return CountIncrease(sumOfThree)

# %% Solution
print("Part-1: number of increase is :", CountIncrease(measurements['Data']))
print("Part-2: number of increase by 3 is :", CountIncreaseBy3(measurements['Data']))
    
    