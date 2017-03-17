import random
import time

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

l = random_list(1, 100, 50)

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
    array = my_array[1:len(my_array)]
    return array

print("Not sorted list: " , l , "\nSorted list: " , insertion_sort(l))
