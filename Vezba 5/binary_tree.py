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
    def __init__(self , root = Node() , left = Node() , right = Node()):
        self.root = root
        self.left = left
        self.right = left

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.data):
            if(node.left != None):
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if(node.right != None):
                self._add(val, node.right)
            else:
                node.right = Node(val)
            return

    def deleteTree(self):
        self.root = None
    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.data):
            return node
        elif(val < node.data and node.left != None):
            self._find(val, node.left)
        elif(val > node.data and node.right != None):
            self._find(val, node.right)

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.lefteft)
            print (str(node.data) + ' ')
            self._printTree(node.right)

tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
print((tree.find(3)).data)
print(tree.find(10))
tree.deleteTree()
tree.printTree()
