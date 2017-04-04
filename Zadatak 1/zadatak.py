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

def heapsort(array):
    global heap_size
    build_max_heap(array)
    for i in range(heap_size-1 ,-1 ,-1):
        array[0] , array[i] = array[i]  , array[0]
        heap_size -= 1
        max_heapify(array , 0)

#Test
print("--------------------------------------------------")
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
print("--------------------------------------------------")

#Radix sort test
print("--------------------------------------------------")
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
print("--------------------------------------------------")

#Heap sort test
print("--------------------------------------------------")
l = random_list(1 , 100 , 50)
sorting_list = l[:]

start_time = time.clock()
heapsort(sorting_list)
end_time = time.clock()

l.sort()

if l == sorting_list:
    print("Heap Sort is correct")
    print("Heap Sort tim: " + str((end_time - start_time)))

l.clear()
sorting_list.clear()
print("--------------------------------------------------")
