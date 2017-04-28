import random

TreeElements = list()

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
        self.parent = None
    def __str__(self):
        return str(self.data) + " " + str(self.left) + " " + str(self.right)

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

    def __init__(self , value):
        self.root = Node(None , None , value)

    def add(self , value , node = None):
        if node == None:
            if self.root != None:
                if self.root.data >= value:
                    if self.root.left == None:
                        self.root.left = Node(None , None , value)
                    else:
                        self.add(value , self.root.left)
                elif self.root.data <= value:
                    if self.root.right == None:
                        self.root.right = Node(None , None , value)
                    else:
                        self.add(value , self.root.right)
            else:
                self.root = Node(None , None , value)
        else:
            if node.data >= value:
                if node.left == None:
                    node.left = Node(None , None , value)
                else:
                    self.add(value , node.left)

            elif node.data <= value:
                if node.right == None:
                    node.right = Node(None , None , value)
                else:
                    self.add(value , node.right)

    def Add(self, x):
        temp = Node(None , None , x)
        if(self.root == None):
            self.root = temp
        else:
            self._Add(self.root, temp)

    def _Add(self, treeNode, newNode):
        if(newNode.data.value <= treeNode.data.value):
            if(treeNode.l == None):
                newNode.p = treeNode
                treeNode.l = newNode
            else:
                self._Add(treeNode.l, newNode)
        else:
            if(treeNode.r == None):
                newNode.p = treeNode
                treeNode.r = newNode
            else:
                self._Add(treeNode.r, newNode)

    def printTree(self , node = None , retVal = ''):
        if(node == None):
            if (self.root == None):
                print("Tree is empty")
            else:
                print("Tree root: " + str(self.root.data) + "\n")
                if(self.root.left != None):
                    self.printTree(self.root.left , retVal)
                if(self.root.right != None):
                    self.printTree(self.root.right , retVal)
        else:
            if (node.data == None):
                print("Node empty\n")
            else:
                print("Node value: " + str(node.data) + "\n")
                if(node.left != None):
                    self.printTree(node.left , retVal)
                if(node.right != None):
                    self.printTree(node.right , retVal)

    def InorderTreeWalk(self , node = None):
        global TreeElements
        if node == None:
            if self.root != None:
                if(self.root.right != None):
                    self.InorderTreeWalk(self.root.right)
                TreeElements.append(self.root.data)
                if(self.root.left != None):
                    self.InorderTreeWalk(self.root.left)
        else:
            if node != None:
                if(node.right != None):
                    self.InorderTreeWalk(node.right)
                TreeElements.append(node.data)
                if(node.left != None):
                    self.InorderTreeWalk(node.left)

    def TreeSearch(self , value , node = None):
        if node == None:
            if self.root == None or value == self.root.data:
                return self.root
            if value < self.root.data:
                return self.TreeSearch(value , self.root.left)
            else:
                return self.TreeSearch(value , self.root.right)
        else:
            if node == None or value == node.data:
                return node
            if value < node.data:
                return self.TreeSearch(value , node.left)
            else:
                return self.TreeSearch(value , node.right)

    def TreeMaximum(self):
        retVal = self.root
        while retVal.right != None:
            retVal = retVal.right
        return retVal

    def _max(self, treeNode):
        if(treeNode.r == None):
            return treeNode
        else:
            return self._max(treeNode.r)

    def TreeMinimum(self):
        retVal = self.root
        while retVal.left != None:
            retVal = retVal.left
        return retVal

    def _min(self, treeNode):
        if(treeNode.l == None):
            return treeNode
        else:
            return self._min(treeNode.l)

    #Following code doesn't work. Done only for practice
    def Transplant(self , u , v):
        if(u.parent == None):
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent

    def TreeDelete(self , z):
        if z.left == None:
            self.Transplant(T , z  , z.right)
        elif z.right == None:
            self.Transplant(T , z , z.left)
        else:
            y = self._min(z.right)
            if y.parent != z:
                self.Transplant(T , y , y.right)
                y.right , y.right.parent = z.right , y
            self.Transplant(T , z , y)
            y.left = z.lefty
            y.left.parent = y


t = Tree(5)

for i in range(0 , 50):
    t.add(random.randrange(0 , 91))
t.add(100)
print("List Before InorderTreeWalk: " , TreeElements)
t.InorderTreeWalk()
print("List After InorderTreeWalk: " , TreeElements)
TreeElements.sort()
print("List After Sort: " , TreeElements)
