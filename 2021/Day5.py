# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 12:04:36 2021

@author: b.sereeter
"""

Inputs = open("Inputs/Day5.txt", "r").read().splitlines()


def GetParameters(line):
    s1, s2 = line.split(" -> ")
    x1, y1 = map(int, s1.split(","))
    x2, y2 = map(int, s2.split(","))
    return x1, x2, y1, y2

def SolvePart1():
    di = {}
    for line in Inputs:
        x1, x2, y1, y2 = GetParameters(line)
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                di[(x1, y)] = 1 if (x1, y) not in di else di[(x1, y)] + 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                di[(x, y1)] = 1 if (x, y1) not in di else di[(x, y1)] + 1
    return len([each for each in di if di[each] > 1])

def SolvePart2():
    di = {}
    for line in Inputs:
        x1, x2, y1, y2 = GetParameters(line)
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                di[(x1, y)] = 1 if (x1, y) not in di else di[(x1, y)] + 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                di[(x, y1)] = 1 if (x, y1) not in di else di[(x, y1)] + 1
        elif abs(x1-x2) == abs(y1-y2):
            dx = -1 if x1 > x2 else 1
            dy = -1 if y1 > y2 else 1
            x, y = x1, y1
            while 1:
                di[(x, y)] = 1 if (x, y) not in di else di[(x, y)] + 1
                if (x, y) == (x2, y2): break
                x += dx
                y += dy
    return len([each for each in di if di[each] > 1])

print("Part-1 :", SolvePart1())
print("Part-2 :", SolvePart2())