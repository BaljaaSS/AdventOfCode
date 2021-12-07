# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 06:07:42 2021

@author: b.sereeter
"""

import pandas as pd
Lines = list(open('Inputs/Day3.txt', 'r').read().splitlines())
Numbers = pd.DataFrame(Lines, columns =['number'])
Numbers = list(Numbers['number'].str)
# %% Part1
def get_index_positions(list_of_elems, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            index_pos = list_of_elems.index(element, index_pos)
            # Add the index position in list
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    return index_pos_list

def MapToDecimal(bin1, bin2):
    bin1Str = "".join(list(map(str, bin1)))
    bin2Str = "".join(list(map(str, bin2)))
    return int(bin1Str,2)*int(bin2Str,2)

def ComputeRateForGammaAndEps(numbers):
    gamma = []
    eps = []
    for num in numbers:
        num = num.tolist()
        one = num.count('1')
        zero = num.count('0')  
        if one >zero:
            gamma.append(1)
            eps.append(0)
        else:
            gamma.append(0)
            eps.append(1)
            
    print(gamma)
    print(eps)            
    return MapToDecimal(gamma, eps)

def FindCo2Rate(lines, it):
    num = [lip[it] for lip in lines]
    one = num.count('1')
    zero = num.count('0')
    if one >= zero:
        ind = get_index_positions(num, '0')
    else:
        ind = get_index_positions(num, '1')
    return [lines[i] for i in ind]

# %% Part2
def FindOxygenRate(lines, it):
    num = [lip[it] for lip in lines]
    one = num.count('1')
    zero = num.count('0')
    if one >= zero:
        ind = get_index_positions(num, '1')
    else:
        ind = get_index_positions(num, '0')
    return [lines[i] for i in ind]

def ComputeRateForOxygenAndCO2(lines):
    oxygen = lines.copy()
    co2 = lines.copy()
    it_o = 0
    it_c = 0
    while (len(oxygen)>1):
        oxygen = FindOxygenRate(oxygen, it_o)
        it_o += 1
    while (len(co2)>1):
        co2 = FindCo2Rate(co2, it_c)
        it_c += 1
        
    print(oxygen)
    print(co2)                    
    return MapToDecimal(oxygen, co2)

# %% Solution
print("Part-1: power consumption is :", ComputeRateForGammaAndEps(Numbers) )
print("Part-2: power consumption is :", ComputeRateForOxygenAndCO2(Lines))
    
    