import random
import time
import sys

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

l = random_list(1, 100, 50)

def sanity_check(array , sorted_array):
    array.sort()
    for i in range(len(array)):
        if(array[i] != sorted_array[i]):
            print("Function hasn't been sorted correctly")
            return
    print("Function has been sorted correctly")



def insertion_sort(array):
    my_array = ["dummy"]
    for i in range(len(array)):
        my_array.append(array[i])
    print("Starting Insertion Sort")
    for j in range(2 , len(my_array)):
        key = my_array[j]
        i = j - 1
        while i > 0 and my_array[i] > key:
            my_array[i + 1] = my_array[i]
            i = i - 1
        my_array[i + 1] = key
    print("Insertion sort has ended")
    return my_array[1:len(my_array)]

def merge(array , p , q , r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    for i in range(1 , n1 + 1):
        L[i].append(array[p + i - 1])
    for j in range(1 , n2 + 1):
        R[j].append(array[q + j])
    L[n1 + 1].append(maxsize)
    R[n2 + 1].append(maxsize)
    i = 1
    j = 1
    for k in range(p , r + 1):
        if L[i] <= R[j]:
            array[k] = L[i]
            i = i + 1
        else:
            array[k] = R[j]
            j = j + 1


def merge_sort(my_array , start , end):
    if start < end:
        q = (start + end)//2
        merge_sort(my_array, start , q)
        merge_sort(my_array, q + 1 , end)
        merge(my_array, start , q , end)
    else:
        return my_array[1:len(my_array)]

my_array = ["dummy"]
for i in range(len(l)):
    my_array.append(l[i])

sanity_check(my_array , merge_sort(my_array , 1 , len(l) - 1))
