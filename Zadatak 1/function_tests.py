import zadatak

#Test
times = {}

print("--------------------------------------------------")
#Selection sort test
l = random_list(1, 100, 50)
sorting_list = l[:]

start_time = time.clock()
selection_sort(sorting_list)
end_time = time.clock()
times.update({"Selection sort" : end_time - start_time})
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
times.update({"Radix sort" : end_time - start_time})
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
heap_sort(sorting_list)
end_time = time.clock()
times.update({"Heap sort" : end_time - start_time})
l.sort()

if l == sorting_list:
    print("Heap Sort is correct")
    print("Heap Sort tim: " + str((end_time - start_time)))

l.clear()
sorting_list.clear()
print("--------------------------------------------------")
print("--------------------------------------------------")
print("Time comparisons: ")
sorted(times.items(), key=lambda x: x[1])
i = 0
for item in times:
    print(str(i+1) , ". " , item)
    i += 1;
