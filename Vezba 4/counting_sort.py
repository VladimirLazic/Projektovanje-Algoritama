import sys
import random
import math
import time
import itertools

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def counting_sort(A , B , k):
    C = [None]*(k+1)
    for i in range(0 , k + 1):
        C[i] = 0
    for j in range(0 , len(A)):
        C[A[j]] = C[A[j]] + 1
    for i in range(0 , k + 1):
        C[i] = C[i] + C[i - 1]
    for j in range(len(A)-1 , -1 , -1):
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1

x=random_list(0, 100, 50)
b=[None]*max(x)
start_time=time.clock()
counting_sort(x,b,max(x))
end_time=time.clock()
b=[x for x in b if x is not None]
x.sort()
if(x==b):
    print("Countingsort was correct")
    print("Countingsort time: "+str((end_time-start_time)))
x.clear()
b.clear()
