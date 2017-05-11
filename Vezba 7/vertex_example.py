from enum import Enum

TIME = 0

class Data:
    """
    Graph data: Any object which is used as a graph vertex data
    """
    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.a1 = val1
        self.a2 = val2

class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, name):
        self.name = name
        self.color = VertexColor.WHITE
        self.parent = None
        self.data = None


    def __repr(self):
        return "{2}:{0} Data: {1}".format(self.color , self.data , self.name)

    def reset(self):
        self.color = VertexColor.WHITE
        self.parent = None
        self.data = {
            'Discovery' : None,
            'Finish' : None
        }

    def increment(self , vertex):
        self.data = vertex.data + 1

def DepthFirstSearch(graph: Dict[Vertex , List[Vertex]] , toplist: List[Vertex] = None):
    for vertex in graph.keys():
        vertex.reset()
    global TIME
    TIME = 0
    for vertex in graph.keys():
        if vertex.color is Color.WHITE:
            DFS_visit(graph , vertex , toplist)

def DFS_visit(graph: Dict[Vertex , List[Vertex]] , element: Vertex , toplist: List[Vertex] = None):
    global TIME
    TIME = TIME + 1

    element.data['Discovery'] = TIME
    element.color = Color.GRAY

    for vertex in graph[element]:
        if vertex.color is Color.WHITE:
            vertex.parent = element
            DFS_visit(graph , vertex , toplist)

    element.color = Color.BLACK
    TIME = TIME + 1
    element.data['Finish'] = TIME

    if toplist is not None:
        toplist.insert(0 , element)

def PrintPath(source: Vertex , destination: Vertex):
    if source == destination:
        print(source)
    elif destination.parent is None:
        print("No path found")
    else:
        PrintPath(source , destination.parent)
        print(destination)


def BreadthFirstSearch(graph : Dict[Vertex , Vertex] , source : Vertex):
    source.reset()
    vertex_queue = queue.Queue()

    for vertex in graph.keys():
        if vertex != source:
            vertex.reset()

    source.color = Color.GRAY
    global TIME
    TIME = 0

    source.data['Discovery'] = TIME
    source.parent = None
    vertex_queue.put(source)

    while not vertex_queue.empty():
        vertex_source = vertex_queue.get()

        for vertex in graph[vertex_source]:
            if vertex.color is Color.WHITE:
                vertex.color = Color.GRAY
                vertex.parent = vertex_source
                vertex_queue.put(vertex)
                TIME = TIME + 1
                vertex.data['Finish'] = TIME

        TIME += 1
        vertex_source.color = Color.BLACK
        vertex_source.data['Finish'] = TIME
        








u = Vertex(c=VertexColor.WHITE, d1=1, d2=22)
v = Vertex(c=VertexColor.GRAY, p=u, d1=33, d2=4)
