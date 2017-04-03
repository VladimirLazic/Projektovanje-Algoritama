import random
import time
import sys
import math

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
    L = list()
    R = list()
    for i in range(0 , n1):
        L.append(array[p + i])

    for j in range(0 , n2):
        R.append(array[q + j ])

    L.append(sys.maxsize)
    R.append(sys.maxsize)
    i = 0
    j = 0
    for k in range(p , r + 1):
        if L[i] <= R[j]:
            array[k] = L[i]
            i = i + 1
        else:
            array[k] = R[j]
            j = j + 1


def merge_sort(my_array , start , end):
    if start < end:
        #q = (start + end)//2
        q = math.floor((start + end)/2)
        merge_sort(my_array, start , q)
        merge_sort(my_array, q + 1 , end)
        merge(my_array, start , q , end)
    else:
        return my_array

def linear_search(data_list , target):
    target_index = -1
    for i in range(0 , len(data_list)):
        if(target == data_list[i]):
            target_index = i
            break
    if(i != -1):
        print("Target found ")
        print("List[" , target_index , "] = " , data_list[target_index])
    else:
        print("Target not in the list!")

def binary_search(sorted_list , target , start):
    q = (start + len(sorted_list) - 1)//2
    target_index =  - 1
    if(target == sorted_list[q]):
        print("Target found")
        target_index = q + start
        print("List[" , target_index , "] = " , sorted_list[q])
    elif (target < sorted_list[q]):
        binary_search(sorted_list[0:q - 1] , target , 0)
    else:
        binary_search(sorted_list[q + 1:] , target , q + 1)


l.sort()
binary_search(l , 99 , 0)
linear_search(l , 99)
