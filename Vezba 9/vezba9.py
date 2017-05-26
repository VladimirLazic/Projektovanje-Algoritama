from enum import Enum
from typing import Dict , List
import sys
import math
import queue
import random

def CutRod(price : List , node_value : int):
    if node == 0:
        return 0
    q = math.inf
    for i in range(0 , n):
        if q > price[i] + CutRod(p , n - 1):
            q = q
        else:
            q = price[i] + CutRod(p , n - 1)
    return q

def MemoizationCutRodAux(p : List , n : int , r : List):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = - math.inf
        for i in range(0 , n):
            if q > price[i] + MemoizationCutRodAux(p , n - 1 , r):
                q = q
            else:
                q = price[i] + MemoizationCutRodAux(p , n - 1 , r)
    r[n] = q
    return q

def MemoizedCutRod(p : List , n : int):
    r = list()
    for i in range(0 , n):
        r.append(- math.inf)
    return MemoizationCutRodAux(p , n  , r)

def BottomUpCutRod(p : List , n : int):
    r = list()
    for j in range(0 , n):
        q = -math.inf
        for i in range(0 , j):
            q = max(q , p[i] + r[j - i])
        r[j] = q
    retrun r[n]

def ExtendedBottomUpCutRod(p : List , n : int):
    r , s = list() , list()
    r.append(0)
    for j in range(0 , n):
        q = -math.inf
        for i in range(0 , j):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
        return r and s

def PrintCutRodSolution(p : List , n : int):


rod = {
    1 : random.randrange(0 , 100),
    2 : random.randrange(0 , 100),
    3 : random.randrange(0 , 100),
    4 : random.randrange(0 , 100),
    5 : random.randrange(0 , 100),
    6 : random.randrange(0 , 100),
    7 : random.randrange(0 , 100),
    8 : random.randrange(0 , 100),
    9 : random.randrange(0 , 100),
    10 : random.randrange(0 , 100)
}

print(rod)
