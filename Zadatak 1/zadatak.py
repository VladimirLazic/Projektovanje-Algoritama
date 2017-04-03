import sys
import random
import math
import time

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

#Selection sort
def selection_sort(A):
    n = len(A)
    for j in range(0 , n-1):
        min = j
        for i in range(j+1 , n):
            if A[i] < A[min]:
                min = i
        if min != j:
            A[j] , A[min] = A[min] , A[j]

#Radix sort
def radix_sort(A):
    n = len(A)
    modules = 10
    div = 1
    while True:
        buckets = [list() for _ in range(10)]

        for item in A:
            least_digit = item % modules
            least_digit = int(least_digit / div)
            buckets[least_digit].append(item)

        modules = modules * 10
        div = div * 10

        if len(buckets[0]) == len(A):
            return buckets[0]

        A = []
        for item in buckets:
            for x in item:
                A.append(x)

#Heap sort

#Test

#Selection sort test
l = random_list(1, 100, 50)
sorting_list = l[:]

start_time = time.clock()
selection_sort(sorting_list)
end_time = time.clock()
l.sort()

if l == sorting_list:
    print("Selection Sort is correct")
    print("Selection Sort tim: " + str((end_time - start_time)))

l.clear()
sorting_list.clear()

#Radix sort
l = random_list(1, 100, 50)
sorting_list = l[:]

start_time = time.clock()
sorting_list = radix_sort(sorting_list)
end_time = time.clock()
l.sort()

if l == sorting_list:
    print("Radix Sort is correct")
    print("Radix Sort tim: " + str((end_time - start_time)))

l.clear()
sorting_list.clear()
