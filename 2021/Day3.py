# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 06:07:42 2021

@author: b.sereeter
"""

import pandas as pd
import Methods as met

Lines = list(open('Inputs/Day3.txt', 'r').read().splitlines())
Numbers = pd.DataFrame(Lines, columns =['number'])
Numbers = list(Numbers['number'].str)

print("Part-1: power consumption is :", met.ComputeRateForGammaAndEps(Numbers) )
print("Part-2: power consumption is :", met.ComputeRateForOxygenAndCO2(Lines))
    
    