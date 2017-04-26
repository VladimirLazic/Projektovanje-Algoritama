import sys

class Node:
    """
    Tree node: left child, right child and data
    """
    def __init__(self, l = None, r = None, d = None):
        """
        Node constructor
        @param A node data object
        """
        self.left = l
        self.right = r
        self.data = d

    def printNode(self):
        print("Node element: " , self.data , "\nNode left: " , self.left , "\nNode right: " , self.right)

class Data:
    """
    Tree data: Any object which is used as a tree node data
    """
    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.a1 = val1
        self.a2 = val2


class Tree:

    #Creating a tree
    def __init__(self , root = Node()):
        self.root = root

    def add_number(self , item):
        if(self.root == None):
            self.root = Node(None , None , item)
        else:
            self._add(self.root , item)

    def _add(self , treeNode , item):
        if(treeNode.data >= item):
            if(treeNode.left == None):
                treeNode.left = Node(None , None , item)
            else:
                self._add(treeNode.left , item)
        elif(treeNode.data < item):
            if(treeNode.right == None):
                treeNode.right = Node(None , None , item)
            else:
                self._add(treeNode.right , item)

    def __str__(self):
        return self.printTree()

    def printTree(self):
        if(self.root == None):
            return "Tree is empty"
        else:
            return self._printTree(self.root , "")

    def _printTree(self , treeNode , retVal):
        if(treeNode != None):
            if(self._printTree(treeNode.left , retVal) != None):
                retVal = self._printTree(treeNode.left , retVal)
            retVal += str(treeNode.data) + "\n"
            if(self._printTree(treeNode.right , retVal) != None):
                retVal = self._printTree(treeNode.right , retVal)
        return retVal

    def treeSearch(self , key , node = None):
        if(node == None):
            if(key == None or self.root.data == key):
                return self.root
            elif(key < self.root.data):
                return self.treeSearch(key , self.root.left)
            else:
                return self.treeSearch(key , self.root.right)
        else:
            if(node.data == key):
                return node
            elif(key < node.data):
                return self.treeSearch(key , node.left)
            else:
                return self.treeSearch(key , node.right)

    def iterative_tree_search(self , node , key):
        temp = node
        while(temp != None and temp.root.data != key):
            if(key < temp.root.data):
                temp = temp.l
            elif(key > temp.root.data):
                temp = temp.r
        return temp

t = Tree(Node(None , None , 5))
print("Root: " , t.root.data , " Left: " , t.root.left , " Right: " , t.root.right)

t.add_number(10)
t.add_number(15)
t.add_number(20)
t.add_number(25)
t.add_number(20)
t.add_number(15)
t.add_number(10)
print(t.printTree())
element = t.treeSearch(20)
if(element != None):
    print("Element found: ")
    element.printNode()
else:
    print("Element not found")
