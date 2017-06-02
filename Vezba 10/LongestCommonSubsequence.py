import sys
import random
import math

def LCS(S : list , n : int , T : list , m : int):
    if n == 0 or m == 0:
        return 0
    if S[n] == T[m]:
        return 1 + LCS(S , n - 1 , T , m - 1)
    else:
        return max(LCS(S , n - 1 , T , m) , LCS(S , n , T , m - 1))

def LCS_Length(X : list , Y : list):
    m , n = len(X) , len(Y)
    b = [[0 for x in range(0 , m)] for y in range(0 , n)]
    c = [[0 for x in range(0 , m)] for y in range(0 , n)]

    for i in range(0 , m):
        for j in range(0 , n):
            if X[i] == Y[j]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "UP-RIGHT"
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "UP"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "RIGHT"
        return (c , b)

def PrintLCS(b : list  , X : list , i : int , j : int):
    if i == 0 or j == 0:
        return
    if b[i][j] ==  "UP-RIGHT":
        PrintLCS(b , X , i - 1 , j - 1)
        print(X[i])
    elif b[i][j] == "UP":
        PrintLCS(b , X , i - 1 , j)
    else:
        PrintLCS(b , X , i , j - 1)


S = [1 , 1 , 1 , 5 , 5 , 3 , 3 , 3 , 3 , 5, 5 , 5, 5,]
T = [1 , 2 , 2 , 3 , 3 , 3 , 3 , 4 , 5 , 5 , 5 , 5, 5]

(c , b) = LCS_Length(S , T)

PrintLCS(b , S , len(S) - 1 , len(T) - 1)
