# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:17:11 2021

@author: b.sereeter
"""
Numbers = [int(i) for i in open('Inputs/Day6.txt', 'r').read().split(',')]

def CountTotalFishes(numbers, days):
    for i in range(0, days):
        # print(i)
        for i in range(0, len(numbers)):
            if(numbers[i] == 0):
                numbers[i] = 6
                numbers.append(8)
            else:
                numbers[i] -= 1
    return len(numbers)

def CountTotalFishesSmartly(numbers, days):
    count = [0] * 9
    for x in Numbers:
        count[x] += 1
    for i in range(256):
        x = count[0]
        count = [count[i+1] for i in range(8)]
        count += [0]
        count[6] += x
        count[8] += x
    return sum(count)
        
print("Part-1: total fish is:", CountTotalFishes(Numbers.copy(), 80))
print("Part-2: total fish is:", CountTotalFishesSmartly(Numbers.copy(), 256))