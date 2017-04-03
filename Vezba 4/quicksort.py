import sys
import random
import math
import time

def sanity_check(array , sort_function):
    my_array = array
    array.sort()
    sort_function(my_array , 0 , len(my_array) - 1)
    for i in range(len(array)):
        if array[i] != my_array[i]:
            print("Sort failed")
            return
    print("Sort successful")

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def partition(A , p , r):
    x = A[r]
    i = p - 1
    for j in range(p , r):
        if A[j] <= x:
            i = i + 1
            A[i] , A[j] = A[j] , A[i]
    A[i + 1] , A[r] = A[r] , A[i + 1]
    return i + 1

def randomized_partition(A , p , r):
    i = random.randint(p , r)
    A[r] , A[i] = A[i] , A[r]
    return partition(A , p , r)

def randomized_quicksort(A , p , r):
    if p < r:
        q = randomized_partition(A , p , r)
        randomized_quicksort(A , p , q - 1)
        randomized_quicksort(A , q + 1 , r)

l = random_list(1, 100, 50)
sanity_check(l , randomized_quicksort)
