import random
import time
import math
import sys

def Parent(i):
    return (i-1)//2

def Left(i):
    return 2*i+1

def Right(i):
    return 2*i+2

def MaxHeapify(A,i):
    l=Left(i)
    r=Right(i)
    if l<size and A[l]>A[i]:
        largest= l
    else:
        largest = i
    if r<size and A[r]>A[largest]:
        largest=r
    if largest!= i:
        A[i],A[largest]=A[largest],A[i]
        MaxHeapify(A,largest)

def BuildMaxHeap(A):
    global size
    size=len(A)
    itterate=len(A)//2-1
    for i in range(itterate,-1,-1):
        MaxHeapify(A,i)

def HeapSort(A):
    global size
    BuildMaxHeap(A)
    for i in range(len(A)-1,0,-1):
        A[0],A[i]=A[i],A[0]
        size-=1
        MaxHeapify(A,0)


def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def HeapMaximum(A):
    return A[0]

def HeapExtractMax(A):
    global size
    if size < 0:
        print("Heap underflow")
    max=A[0]
    A[0] = A[size-1]
    size -=1
    MaxHeapify(A,0)
    return max

def MaxHeapInsertKey(A,key):
    global size
    size+=1
    A.append(-sys.maxsize)
    HeapIncreaseKey(A,size-1,key)

def HeapIncreaseKey(A,i,key):
    if key<A[i]:
        print("new Key is smaller than current key")
    A[i]=key
    while i > 0 and A[Parent(i)]< A[i]:
        A[i],A[Parent(i)]=A[Parent(i)],A[i]
        i=Parent(i)

size=int()
A=list()
A=random_list(0,100,5)
print("List: " , A)
BuildMaxHeap(A)
print("Build-max heap: " , A)
#A.append(1)
#A.append(2)
#A.append(3)
#A.append(4)
#A.append(5)
#print("Random container: ",A)
#start_time = time.clock()
#HeapSort(A)
#end_time = time.clock()
#print("Sorted container: ",A)
#print("Time: ",(end_time-start_time))
#BuildMaxHeap(A)
#MaxHeapInsertKey(A,40)
#print(HeapExtractMax(A))
#print(A)
