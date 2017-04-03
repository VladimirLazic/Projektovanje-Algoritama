import sys
import random
import math
import time
import itertools

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def InsertionSort(A):
    if len(A) <= 1: return A
    i = 1
    while i < len(A):
        k = A[i]
        j = i - 1
        while j >= 0 and A[j] > k:
            A[j+1] = A[j]
            A[j] = k
            j -= 1
        i += 1
    return A

def bucket_sort(A):
    n=len(A)
    B=[None]*(n)
    for i in range(0,n):
        B[i]=list()
    for i in range(0,n):
        B[int(n*A[i])].append(A[i])
    for i in range(0,n):
        InsertionSort(B[i])
    return list(itertools.chain(*B))

def sanity_check(array , sort_function):
    array[:] = [i / 100 for i in array]
    my_array = sort_function(array)
    array.sort()
    for i in range(len(array)):
        if array[i] != my_array[i]:
            print("Sort failed")
            return
    print("Sort successful")

l = random_list(1, 100, 50)
sanity_check(l , bucket_sort)

x=random_list(0, 100, 50)
x[:] = [i / 100 for i in x]
b=x[:]
start_time=time.clock()
x=bucket_sort(x)
end_time=time.clock()
b.sort()
if b==x:
    print("Bucketsort was correct")
    print("Bucketsort time: "+str((end_time-start_time)))
x.clear()
b.clear()
