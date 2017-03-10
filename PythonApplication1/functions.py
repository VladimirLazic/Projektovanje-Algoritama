import sys

#First
def sum_of_first_N(n): 
    retVal = 0 
    for i in range(n):
        retVal += i
    return retVal 

#Second
def sum_of_first_N_squared(n):
    retVal = 0
    for i in range(n):
        retVal += i**2
    return retVal

#Third
def input_print():
    if len(sys.argv) < 3:
        sys.exit() 
    else:
        print("Uneto dovoljno parametara")
    
    retVal = 0
    retVal = sys.argv[1][0] + sys.argv[1][1] + sys.argv[1][2]
    retVal += sys.argv[2][-1] + sys.argv[2][-2] + sys.argv[2][-3]
    
    return retVal

#Fourth
def first_hundred():
    x = []
    for i in range(1 , 101):
        x.append(i)
    x.reverse()
    print(x)

#Fifth
#TODO: finish this
def number_of_repetition():
    input_file = open("dict_test.txt" , "r")
    dictionary = {}
    for word in input_file.read():
        print(word)
        for key , value in dictionary.items():
            if (key == word):
                value += 1
                break
            else:   
                dictionary[word] = 1

#Sixst

#Seventh   
    

number_of_repetition()