from enum import Enum
import sys
import math
import queue

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, c = None, parent = None, data = None):
        """
        Vertex constructor
        @param color, parent, auxilary data1, auxilary data2
        """
        self.c = c
        self.parent = parent
        self.data = data
        self.edges = list()

    def __lt__(self , vertex : Vertex):
        return self.data < vertex.data

    def addEgde(self , destination : Vertex , weight : int):
        self.edges.append(Edge(self , destination , weight))

class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255

class Edge:
    def __init_(self , source = None , destination = None , weight = None):
        self.source = source
        self.destination = destination
        self.weight = weight

def Initialize_Single_Source(graph : Dict[Vertex , List[Vertex]] , source : Vertex):
    for vertex in graph.keys():
        vertex.data = math.inf
        vertex.parent = None
    source.data = 0

def Relax(u : Vertex , v : Vertex):
    #Find edge
    found_edge = None
    for egde in u.edges:
        if egde.destination is v:
            found_edge = edge

    if found_edge == None:
        print("No path found")
        return

    if v.data > u.data + found_edge.weight:
        v.data = u.data + found_edge.weight
        v.parent = u

def Dijkstra(graph : Dict[Vertex , List[Vertex]] , source : Vertex):
    Initialize_Single_Source(graph , source)

    S = list()
    vertex_list = list()
    for vertex in graph.keys():
        vertex_list.append(vertex)

    while not vertex_list.empty():
        u = min(vertex_list)
        S.append(u)
        for vertex in graph[u]:
            Relax(u , v)






u = Vertex(c=VertexColor.WHITE, d1=1, d2=22)
v = Vertex(c=VertexColor.GRAY, p=u, d1=33, d2=4)
