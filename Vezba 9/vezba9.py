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
