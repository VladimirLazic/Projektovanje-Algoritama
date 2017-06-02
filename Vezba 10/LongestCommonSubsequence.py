import sys
import random
import math
import numpy

def LCS(S : list , n : int , T : list , m : int):
    if n == 0 or m == 0:
        return 0
    if S[n] == T[m]:
        return 1 + LCS(S , n - 1 , T , m - 1)
    else:
        return max(LCS(S , n - 1 , T , m) , LCS(S , n , T , m - 1))

def LCS_Length(X : list , Y : list):
    m , n = len(X) , len(Y)
    b , c = list() , list()
    b = [" " for x in range(0 , m*n)]
    c = [0 for x in range(0 , m*n)]
    print("b" , b)
    print("c"  , c)

    for i in range(0 , m):
        for j in range(0 , n):
            if X[i] == Y[j]:
                c[j*n + i] = c[(j - 1)*n + (i - 1)] + 1
                #numpy.append(b[i][j] , "UP-RIGHT")
                b[j*n + i] = "UP-RIGHT"
            elif c[j*n + i - 1] >= c[(j-1)*n + i]:
                c[j*n + i] = c[j*n + i - 1]
                #numpy.append(b[i][j] , "UP")
                b[j*n + i] = "UP"
            else:
                c[j*n + i] = c[(j-1)*n + i]
                #numpy.append(b[i][j] , "RIGHT")
                b[j*n + i] = "RIGHT"
        return (c , b)

def PrintLCS(b : list  , X : list , i : int , j : int , N : int):
    if i == 0 or j == 0:
        return
    if b[j*N + i] ==  "UP-RIGHT":
        PrintLCS(b , X , i - 1 , j - 1 , N)
        print(b[j*N + i])
    elif b[j*N + i] == "UP":
        #print(b[j*N + i])
        PrintLCS(b , X ,  i - 1 , j , N)
    else:
        #print(b[j*N + i])
        PrintLCS(b , X , i , j - 1 , N)


S = [1 , 1 , 1 , 5 , 5 , 3 , 3 , 3 , 3 , 5, 5 , 5, 5]
T = [1 , 2 , 2 , 3 , 3 , 3 , 3 , 4 , 5 , 5 , 5 , 5, 5]

(c , b) = LCS_Length(S , T)

PrintLCS(b , S , len(S) - 1 , len(T) - 1 , len(T) - 1)
