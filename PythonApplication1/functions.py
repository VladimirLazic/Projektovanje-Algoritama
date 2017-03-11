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
def number_of_repetition():
    input_file = open("dict_test.txt" , "r")
    listOfWords = []
    dictionary = {}
    with input_file as it:
        for line in it:
                for word in line.split():
                        if(not dictionary):
                            dictionary[word] = 1
                        else:
                            if word in dictionary:
                                dictionary[word] += 1
                            else:
                                dictionary[word] = 1
    print(dictionary)
#Sixst
def list_of_tuples():
    list = []
    for i in range(4):
        inputString = input("Unesite int, float i string: ")
        inputInt , inputFloat, inputSubString = inputString.split()
        list.append((int(inputInt) , float(inputFloat) , inputSubString))
    print(list)
    list.pop(0)
    print("New list: " , list)

#Seventh


list_of_tuples()
