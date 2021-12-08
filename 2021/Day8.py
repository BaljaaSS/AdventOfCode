# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 09:54:52 2021

@author: b.sereeter
"""

Input = open("Inputs/Day8.txt", "r").read().splitlines()
    
def SolvePart1():
    ans = 0
    for line in Input:
        s = line.split(" | ")
        for each in s[1].split():
            if len(each) in [2, 3, 4, 7]:
                ans +=1
    return ans
    
print("Part-1: Bingo Number is :", SolvePart1())