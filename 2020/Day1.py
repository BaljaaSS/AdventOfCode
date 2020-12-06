import numpy as np

yearList = np.genfromtxt("AdventOfCode/2020/Input1.txt", usecols=0, usemask=False)

# %% Part-1
shortYearList = yearList
for x in yearList:
    shortYearList = np.delete(shortYearList, 0)
    for y in shortYearList:
        if(x + y == 2020):
            print("Answer for x*y while x+y=2020 is :", x * y)

# %% Part-2
shortYearList = yearList
for x in yearList:
    shortYearList = np.delete(shortYearList, 0)
    shortestYearList = shortYearList
    for y in shortYearList:
        shortestYearList = np.delete(shortestYearList, 0)
        for z in shortestYearList:
            if(x + y + z == 2020):
                print("Answer for x*y*z while x+y+z=2020 is :", x*y*z)
