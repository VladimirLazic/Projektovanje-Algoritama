import queue
import random
import time
import matplotlib.pyplot as plt
from enum import Enum
from typing import Dict , List



TIME = 0

class Color(Enum):
    """Colors used to denote vertex states"""
    BLACK = 0
    GRAY = 127
    WHITE = 255


class Vertex:
    """Graph vertex"""

    def __init__(self, name):
        self.name = name
        self.color = Color.WHITE
        self.parent = None
        self.data = {
            'Start Time' : None ,
            'End Time'   : None
        }

    def __repr__(self):
        Colour = ""
        Parent = ""
        Start_Time = ""
        End_Time = ""

        if self.color is Color.BLACK:
            Colour = 'BLACK'
        elif self.color is Color.GRAY:
            Colour = 'GRAY'
        else:
            Colour = 'WHITE'

        if self.parent is None:
            Parent = " "
        else:
            Parent = self.parent.name

        if self.data['Start Time'] is None:
            Start_Time = ' '
        else:
            Start_Time = "\n\t{}".format(self.data['Start Time'])

        if self.data['End'] is None:
            End_Time = ' '
        else:
            End_Time = "/{}".format(self.data['End Time'])

        return "{0}:\n\tColor: {1}{2}{3}\n\t[{4}]\n".format(self.name,
            Colour , Start_Time , End_Time , Parent)


    def reset(self):
        self.color = Color.WHITE
        self.parent = None
        self.data = {
            'Start Time' : None,
            'End Time'   : None
        }

    def init_start(self):
        if self.data['Start Time'] is None:
            self.data['Start Time'] = 0

    def init_end(self):
        if self.data['End Time'] is None:
            self.data['End Time'] = 0

def DFS(graph : Dict[Vertex , List[Vertex]] , vertex: Vertex , toplist: List[Vertex] = None):
    for vertex in graph.keys():
        vertex.reset()

    time = 0
    for vertex in graph.keys():
        if vertex.color is Color.WHITE:
            DFS_visit(graph , vertex , time , toplist)

def DFS_visit(graph : Dict[Vertex , List[Vertex]] , element : Vertex , time : int , toplist : List[Vertex] = None):
    time += 1

    element.data['Start Time'] = time
    element.color = Color.GRAY

    for vertex in graph[element]:
        if vertex.color is Color.WHITE:
            vertex.parent = element
            DFS_visit(graph , vertex , time , toplist)

    element.color = Color.BLACK
    time += 1
    element.data['End Time'] = time

    if toplist is not None:
        toplist.insert(0 , element)

def PrintPath(graph : Dict[Vertex , List[Vertex]] , source : Vertex ,
              destination : Vertex , option : bool = False):
    if not option:
        BFS(graph , source)
    else:
        DFS(graph , source)

    _print_path(source , destination)
    print()

def _print_path(source : Vertex , destination : Vertex):
    retVal = False

    if source == destination:
        print(source.name)
        retVal = True
        return retVal
    elif destination.parent is None:
        print("No path found")
        return retVal
    else:
        retVal = _print_path(source , destination.parent)
        print(destination.name)
        return retVal

def BFS(graph : Dict[Vertex , Vertex] , source : Vertex):
    source.reset()

    vertex_queue = queue.Queue()
    for vertex in graph.keys():
        if vertex != source:
            vertex.reset()

    source.color = Color.GRAY
    source.init_start()
    source.parent = None
    vertex_queue.put(source)

    while not vertex_queue.empty():
        vertex_source = vertex_queue.get()
        for vertex in graph[vertex_source]:
            if vertex.color is Color.WHITE:
                vertex.color = Color.GRAY
                vertex.parent = vertex_source
                vertex_queue.put(vertex)
                vertex.data['Start Time'] = vertex_source.data['Start Time'] + 1
        vertex_source.color = Color.BLACK


#Testing of functions
VERTEXR = Vertex('R')
VERTEXV = Vertex('V')
VERTEXS = Vertex('S')
VERTEXW = Vertex('W')
VERTEXT = Vertex('T')
VERTEXU = Vertex('U')
VERTEXY = Vertex('Y')
VERTEXX = Vertex('X')
VERTEXZ = Vertex('Z')
#BFS graph
BFSG = {
    VERTEXS: [VERTEXR, VERTEXW],
    VERTEXR: [VERTEXS, VERTEXV],
    VERTEXV: [VERTEXR],
    VERTEXW: [VERTEXS, VERTEXT, VERTEXX],
    VERTEXT: [VERTEXW, VERTEXX, VERTEXU],
    VERTEXX: [VERTEXT, VERTEXW, VERTEXY],
    VERTEXU: [VERTEXT, VERTEXX, VERTEXY],
    VERTEXY: [VERTEXT, VERTEXX, VERTEXU]
    }

BFS(BFSG, VERTEXT)
DFSG = {
    VERTEXU: [VERTEXX, VERTEXV],
    VERTEXX: [VERTEXV],
    VERTEXV: [VERTEXY],
    VERTEXY: [VERTEXX],
    VERTEXW: [VERTEXY, VERTEXS],
    VERTEXS: [VERTEXS]
}



#Analysis
def sum_edges(graph: Dict[Vertex, List[Vertex]]):
    """Returns number of aall edges of a graph"""
    suma = 0
    for keys in graph.keys():
        suma += len(graph[keys])
    return suma

def sum_vertexes(graph: Dict[Vertex, List[Vertex]]):
    """Returns all number of vertexes in graph"""
    return len(graph.keys())

def random_vertices(size, elements):
    """Generate a list of random vertices"""
    verticesnames = random.sample(range(1, size+1), elements)
    vertices = []
    for item in verticesnames:
        #Make a vertex out of every random int
        vertices.append(Vertex(item))
    return vertices

def generate_graph(size: int):
    """Returns randomly generated graph of omitted size
    maximum size is 10000"""
    graph = dict()
    #Generate size number of verticies
    vertices = random_vertices(10000, size)
    #Init graph
    for item in vertices:
        #Put every vertex into the graph
        graph[item] = []
    for item in graph:
        #generate random edges for every vertex
        edgenumber = random.randint(0, size)
        random.shuffle(vertices)
        #assign the edges to the graphs vertex
        graph[item] = vertices[0:edgenumber]
    #return the random graph
    return graph

def first_source(graph: Dict[Vertex, List[Vertex]]):
    """Return a the first vertex in the dictionary"""
    for item in graph:
        return item

def time_measure(graph: Dict[Vertex, List[Vertex]], bfs: bool=False):
    """Returns how long it took for dfs (default) or bfs (set aditonal argument to True)"""
    time_start = 0
    time_end = 0
    if not bfs:
        time_start = time.clock()
        DFS(graph, first_source(graph))
        time_end = time.clock()
    else:
        time_start = time.clock()
        BFS(graph, first_source(graph))
        time_end = time.clock()
    return time_end - time_start

def analyse():
    """Extracts runing times. New graph will be made for every value in runnsize.
     modify runnsize for different size of graphs"""
    vertices = [5, 25, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    exectimebfs = []
    exectimedfs = []
    edges = []
    for item in vertices:
        temp_graph = generate_graph(item)
        # number of edges
        edges.append(sum_edges(temp_graph))
        # extract time for bfs
        exectimebfs.append(time_measure(temp_graph, True))
        # extract time for dfs
        exectimedfs.append(time_measure(temp_graph))
    plot_graph_stats(vertices, edges, exectimebfs, 'Breath-First-Search')
    plot_graph_stats(vertices, edges, exectimedfs, 'Depth-First-Search')

def plot_graph_stats(vertices: List[int], edges: List[int], exec_time: List[int], label: str):
    """Makes plot of graph structure"""
    input_data = []
    for index, item in enumerate(vertices):
        input_data.append(item + edges[index])
    plt.plot(input_data, exec_time, label=label)
    plt.xlabel('V + E [n]')
    plt.ylabel('T[S]')
    plt.legend()
    print(label)
    for index, item in enumerate(vertices):
        print("Number of vertecies: {} Number of edges: {} Time: {}"\
        .format(item, edges[index], exec_time[index]))

analyse()
plt.show()
