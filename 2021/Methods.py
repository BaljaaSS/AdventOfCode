# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 06:52:42 2021

@author: b.sereeter
"""

# %% Day1
def CountIncrease(data):
    count = 0
    previous = data[0]
    for m in data:
        if (m > previous):
            count += 1
        previous = m
    return count

def CountInreaseBy3(data):
    sumOfThree = []
    for i in data.index:
        sumOfThree.append(data[i:i+3].sum())              
    return CountIncrease(sumOfThree)

# %% Day2