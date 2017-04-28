import sys
import random
import math
import time
import numpy as np
import matplotlib.pyplot as plt

stdLenths = [1, 10, 100, 1000, 10000]

def CreatePlot(input_data, exec_time, algo_name, subplotIndex):
    plt.plot(input_data, exec_time, label=algo_name)
    plt.xlabel('Input [n]')
    plt.ylabel('Time [S]')
    plt.legend()
    print(algo_name)
    for i in range(0, len(input_data)):
        print("input_data: ", input_data[i], ", exec_time: ", exec_time[i])

def random_list(min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def isSorted(A):
    testList = A[:]
    testList.sort()
    if testList == A:
        return True
    return False


def analyzeAlgorithm(type, subplotIndex):
    #global stdLenths = [1, 10, 100, 1000, 10000]
    sortTimes = list()
    j = 0
    for i in stdLenths:
        x = random_list(0, 1000000 + 1, i)
        startTime = time.clock()
        if type.__name__ != "radix_sort":
            type(x)
        else:
            x = type(x)
        endTime = time.clock()
        sortTimes.append(endTime - startTime)
        j += 1
    if(isSorted(x)):
        CreatePlot(stdLenths, sortTimes, type.__name__, subplotIndex)

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
def parent(i):
    return int((i-1)/2)

def left(i):
    return 2*i+1

def right(i):
    return 2*i + 2

def max_heapify(array , i):
    l = left(i)
    r = right(i)
    largest = 0
    if l < heap_size and array[l] > array[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and array[r] > array[largest]:
        largest = r
    if largest != i:
        array[i] , array[largest] = array[largest] , array[i]
        max_heapify(array , largest)

def build_max_heap(array):
    global heap_size
    heap_size = len(array)
    for i in range(heap_size//2-1, -1 , -1):
        max_heapify(array , i)

def heap_sort(array):
    global heap_size
    build_max_heap(array)
    for i in range(heap_size-1 ,-1 ,-1):
        array[0] , array[i] = array[i]  , array[0]
        heap_size -= 1
        max_heapify(array , 0)

#Test
times = {}

print("--------------------------------------------------")
#Selection sort test
l = random_list(1, 10000 , 1000)
sorting_list = l[:]

start_time = time.clock()
selection_sort(sorting_list)
end_time = time.clock()
times.update({"Selection sort" : end_time - start_time})
l.sort()

if l == sorting_list:
    print("Selection Sort is correct")
    print("Selection Sort time: " + str((end_time - start_time)))

analyzeAlgorithm(selection_sort, 1)

l.clear()
sorting_list.clear()
print("--------------------------------------------------")

#Radix sort test
print("--------------------------------------------------")
l = random_list(1, 10000 , 1000)
sorting_list = l[:]

start_time = time.clock()
sorting_list = radix_sort(sorting_list)
end_time = time.clock()
times.update({"Radix sort" : end_time - start_time})
l.sort()

if l == sorting_list:
    print("Radix Sort is correct")
    print("Radix Sort time: " + str((end_time - start_time)))

analyzeAlgorithm(radix_sort, 2)

l.clear()
sorting_list.clear()
print("--------------------------------------------------")

#Heap sort test
print("--------------------------------------------------")
l = random_list(1 , 10000 , 1000)
sorting_list = l[:]

start_time = time.clock()
heap_sort(sorting_list)
end_time = time.clock()
times.update({"Heap sort" : end_time - start_time})
l.sort()

if l == sorting_list:
    print("Heap Sort is correct")
    print("Heap Sort time: " + str((end_time - start_time)))

analyzeAlgorithm(heap_sort , 3)
plt.show()

l.clear()
sorting_list.clear()
