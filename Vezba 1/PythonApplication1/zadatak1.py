import sys

if len(sys.argv) > 1:
    print("Parametar prosledjen")
    #print("arg is: " , sys.argv[1])
    name = sys.argv[1]
else:
    print("Parametar nije prosledjen")
    sys.exit()

x = [(1,2) , (3,4) , (5,6) , (7,8) , (9,10)]
print(x)

dictionary = {name:x}
#print("Dictionary : " , dictionary)
for key , value in dictionary.items():
    print("key: " , key , "\nvalue: " , value)