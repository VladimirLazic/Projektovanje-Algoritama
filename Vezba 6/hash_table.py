import sys
import random
import math

KNUTH = (math.sqrt(5) - 1) / 2

class Data:
    """
    Tree data: Any object which is used as a tree node data
    """
    def __init__(self, key, literal):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.key = key
        if literal is None:
            self.literal = chr(self.key)
        else:
            self.literal = literal

    def __str__(self):
        return str(self.key) + " " + str(self.literal)

    def get_key(self):
        return self.key

    def get_literal(self):
        return self.literal

    def toString(self):
        return self.__str__()

class Hash_Table:

    def __init__(self , capacity = 23 , p = 23 , option = 0):
        self.capacity = capacity
        self.slots = []

        for item in range(self.capacity):
            self.slots.append([])
            self.slots[item] = []

        self.p = p
        self.a = random.randrange(1 , p)
        self.b = random.randrange(0 , p)
        self.option = option

    def __str__(self):
        xstring = ""
        for slot in self.slots:
            if len(slot) != 0:
                for index, item in enumerate(slot):
                    if index == len(slot) - 1:
                        xstring += "[" + str(item) + "]\n"
                    else:
                        xstring += "[" + str(item) + "]-->"
            else:
                xstring += '[]\n'
        return xstring

    def __len__(self):
        size = 0
        for item in self.slots:
            size += len(item)
        return size

    def hash(self , key):

        if self.option == 0:
            return key % self.capacity

        if self.option == 1:
            return math.floor(self.capacity * ((key * KNUTH) % 1))

        if self.option == 2:
            return ((self.a * key + self.b) % self.p) % self.capacity

    def insert(self , data):

        slot = self.hash(data.key)
        for item in self.slots[slot]:
            if data.key == item.key:
                item.literal = data.literal
                return -1
        self.slots[slot].append(data)
        return slot

    def searsh(self , key):
        for item in self.slots[self.hash(key)]:
            if item.key == key:
                return item
        return None

    def delete(self , key):

        for index , item in enumerate(self.slots[self.hash(key)]):
            if item.key == key:
                del self.slots[self.hash(key)][index]
                return True
        return False

h_t = Hash_Table()
h_t.insert(Data(0 , 5))
h_t.insert(Data(1 , 50))
h_t.insert(Data(2 , 500))
print(h_t.__str__())
