import numpy as np
from itertools import combinations
yearList = np.genfromtxt(
    "AdventOfCode/2020/Input/Input1.txt", usecols=0, usemask=False, dtype= int)

# %% Part-1
combos = combinations(yearList, 2)
xy = next(c for c in combos if sum(c)==2020)
print("Answer for x*y while x+y=2020 is :", xy[0]*xy[1])

# %% Part-2
combos = combinations(yearList, 3)
xyz = next(c for c in combos if sum(c)==2020)
print("Answer for x*y*z while x+y+z=2020 is :", xyz[0]*xyz[1]*xyz[2])
