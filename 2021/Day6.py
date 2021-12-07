# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:17:11 2021

@author: b.sereeter
"""

Numbers = [int(i) for i in open('Inputs/Day6.txt', 'r').read().split(',')]

def CountTotalFishes(numbers, days):
    for i in range(0, days):
        print(i)
        for i in range(0, len(numbers)):
            if(numbers[i] == 0):
                numbers[i] = 6
                numbers.append(8)
            else:
                numbers[i] -= 1
    return len(numbers)

def CountTotalFishesSmartly(numbers, days):
    sumF = 0
    for i in range(1,6):
        print(i)
        sumF += CountTotalFishes([i], days)*numbers.count(i)        
    return sumF
        
# print("Part-1: total fish is:", CountTotalFishes(Numbers.copy(), 80))
print("Part-2: total fish is:", CountTotalFishesSmartly(Numbers.copy(), 256))

# 1 => 18 = 7 
# 2 => 18 = 5
# 3 => 18 = 5
# 4 => 18 = 4
# 5 => 18 = 4
