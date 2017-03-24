import sys
import math
import random

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

l = random_list(1, 100, 10)

def parent(i):
    return int((i-1)/2)

def left(i):
    return 2*i+1

def right(i):
    return 2*i + 2

def heap_max(array):
    return array[0]

def heap_increase_key(array , i , key):
    if key < array[i]:
        print("Error: New key is smaller than current key")
    array[i] = key
    while i > 0 and array[parent(i)] < array[i]:
        array[i] , array[parent(i)] = array[parent(i)] , array[i]
        i = parent(i)

def heap_extract_max(array):
    if heap_size < 0:
        print("Error: Heap underflow")
    max = array[0]
    array[0] = array[heap_size]
    heap_size -= 1
    max_heapify(array , 0)
    return max

def heap_max_insert(array , key):
    heap_size += 1
    array[heap_size] = - sys.maxsize
    heap_icrease_key(array , heap_size , key)

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

heap_size = int()
print("First list: " , l)
build_max_heap(l)
print("Build-heap test:" , l)
#heapsort(l)
#print("Heap-sorted: " , l)
