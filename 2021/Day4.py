# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 10:47:45 2021

@author: b.sereeter
"""
import numpy as np

RNumbers = open('Inputs/Day4_RandomNumbers.txt', 'r').read().split(',')
RNumbers = [int(i) for i in RNumbers]

with open('Inputs/Day4.txt', 'r') as Input:
    Lines = [col.split() for col in Input.read().splitlines()]
  
def ConvertToMatrix(lines):
    mSize = len(lines[0])
    boards = []
    for i in range(0, len(lines), 6):
        matrix = np.array(Lines[i:i + mSize]).astype(np.int64())
        boards.append(matrix)
    return boards

def ConvertToRowCol(boards):
    boardsByList = []
    for board in boards:
        l = list(board)
        l = l + list(board.T)
        blist = []
        for j in l:
            blist.append([j.tolist(), 0])
        boardsByList.append([blist, np.sum(board), False]) 
    return boardsByList

def Count(blist, rn):
    stop = False
    subSum = False
    for b in blist:
        if (rn in b[0]):
            b[1] +=1
            subSum = True
        if(b[1]==5):
            stop = True
    return blist, stop, subSum

def CountToList(blist, rn, sumT):
    stop = False
    subSum = False
    for b in blist:
        if (rn in b[0]):
            b[1] +=1
            subSum = True
        if(b[1]==5):
            sumT -= 1
        if sumT == 1:
            stop = True
    return blist, stop, subSum

def PlayBingo(lines, rNumbers):
    boardsByMatrix = ConvertToMatrix(lines.copy())
    boardsByList = ConvertToRowCol(boardsByMatrix.copy())
    sumM = 0
    sumT = len(boardsByList)
    rNumStoped = 0
    for rn in rNumbers:
        # print(rn)
        stop1 = False
        for board in boardsByList:
            board[0], stop2, subSum = CountToList(board[0].copy(), rn, sumT)
            if(subSum):
                board[1] -= rn   
            if (stop2):
                sumM = board[1]
                stop1 = True
                break
        if (stop1):
            rNumStoped = rn
            break
    print(sumM)
    print(rNumStoped)        
    return sumM*rNumStoped

print("Part-1: Bingo Number is :", PlayBingo(Lines, RNumbers))
# print("Part-2: Bingo Number is :", PlayBingoToLose(Lines, RNumbers))