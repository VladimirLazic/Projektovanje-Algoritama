from enum import Enum
from typing import Dict , List
import sys
import math
import queue

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, id : int , parent = None , data = None):
        """
        Vertex constructor
        @param color, parent, auxilary data1, auxilary data2
        """
        self.id = id
        self.parent = parent
        self.data = data
        self.edges = list()

    def __lt__(self , vertex):
        return self.data < vertex.data

    def addEdge(self , destination , weight : int):
        self.edges.append(Edge(self , destination , weight))

class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255

class Edge:
    def __init__(self , source = None , destination = None , weight = None):
        self.source = source
        self.destination = destination
        self.weight = weight

def Initialize_Single_Source(graph : List[Vertex] , source : Vertex):
    for vertex in graph:
        vertex.data = math.inf
        vertex.parent = None
    source.data = 0

def Relax(u : Vertex , v : Vertex, shortest_path : int):
    #Find edge
    found_edge = None
    for edge in u.edges:
        if edge.destination is v:
            found_edge = edge

    print("\n\nFound edge: " , found_edge.destination.data , "\tEgde weight: " , found_edge.weight)

    if found_edge == None:
        print("No path found")
        return

    if v.data > u.data + found_edge.weight:
        v.data = u.data + found_edge.weight
        v.parent = u
        shortest_path += found_edge.weight

def Dijkstra(graph : List[Vertex] , source : Vertex):
    Initialize_Single_Source(graph , source)

    S = list()
    vertex_list = list()
    for vertex in graph:
        vertex_list.append(vertex)

    shortest_path = 0
    while vertex_list:
        u = min(vertex_list)
        S.append(u)

        for egde in u.edges:
            Relax(u , egde.destination , shortest_path)
        vertex_list.remove(u)
    return shortest_path


#Testing the functions
VERTEX_s = Vertex(0)
VERTEX_t = Vertex(math.inf)
VERTEX_y = Vertex(math.inf)
VERTEX_x = Vertex(math.inf)
VERTEX_z = Vertex(math.inf)

#Creating paths
VERTEX_s.addEdge(VERTEX_t , 10)
VERTEX_s.addEdge(VERTEX_y , 5)

VERTEX_t.addEdge(VERTEX_y , 2)
VERTEX_t.addEdge(VERTEX_x , 1)

VERTEX_y.addEdge(VERTEX_t , 3)
VERTEX_y.addEdge(VERTEX_x , 9)
VERTEX_y.addEdge(VERTEX_z , 2)

VERTEX_x.addEdge(VERTEX_z , 4)

VERTEX_z.addEdge(VERTEX_x , 6)
VERTEX_z.addEdge(VERTEX_s , 7)

graph = [VERTEX_s , VERTEX_t , VERTEX_y , VERTEX_x , VERTEX_z]

for vertex in graph:
    print("Vertex :" , vertex.id , "\t Edges : ")
    for egde in vertex.edges:
        print("\t" , egde.destination.id)

print("Shortest path is :" , Dijkstra(graph , VERTEX_s))
