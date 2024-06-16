#Kacper Cieśla - 414796
#Nieskończone

import graf_mst

class Vertex:
    def __init__(self, key, color=None):
        self.key = key
        self.color = color
        self.intree = False
        self.distance = float('inf')
        self.parent = None

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return str(self.key)

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color


class Edge:
    def __init__(self, vertex1, vertex2, weight=None):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

class ListGraph:
    def __init__(self):
        self.dict = {}

    def is_empty(self):
        return len(self.dict.keys()) == 0

    def insert_vertex(self, vertex):
        if vertex not in self.dict.keys():
            self.dict[vertex] = {}

    def insert_edge(self, vertex1, vertex2, edge=None):
        self.insert_vertex(vertex1)
        self.insert_vertex(vertex2)
        self.dict[vertex1][vertex2] = edge
        self.dict[vertex2][vertex1] = edge

    def delete_vertex(self, vertex):
        if vertex in self.dict:
            del self.dict[vertex]
            for key in self.dict:
                if vertex in self.dict[key]:
                    del self.dict[key][vertex]

    def delete_edge(self, vertex1, vertex2):
        if vertex1 in self.dict and vertex2 in self.dict:
            if vertex2 in self.dict[vertex1]:
                del self.dict[vertex1][vertex2]
            if vertex1 in self.dict[vertex2]:
                del self.dict[vertex2][vertex1]

    def neighbours(self, vertex_id):
        if vertex_id in self.dict:
            return self.dict[vertex_id].items()

    def get_vertex(self, vertex_id):
        return vertex_id

    def vertices(self):
        return self.dict.keys()

class MST:
    def __init__(self, graph, start_vertex=None):
        self.graph = graph
        self.edges = []
        self.start_vertex = start_vertex
        if self.start_vertex is None:
            self.start_vertex = next(iter(self.graph.vertices()), None)
        for vertex in self.graph.vertices():
            self.graph.insert_vertex(vertex)
        self.prim(self.graph, start_vertex)

    def prim(self, graph, start_vertex):
        if start_vertex is None:
            return
        start_vertex.intree = True
        start_vertex.distance = float('inf')
        current_vertex = start_vertex
        while current_vertex is not None:
            for neighbor, weight in graph.neighbours(current_vertex):
                if not neighbor.intree and weight < neighbor.distance:
                    neighbor.distance = weight
                    neighbor.parent = current_vertex

            edge = Edge(current_vertex, current_vertex.parent, current_vertex.distance)
            self.edges.append(edge)
            self.graph.insert_edge(current_vertex, current_vertex.parent, current_vertex.distance)
            current_vertex.intree = True

            current_vertex = None
            for vertex in graph.vertices():
                if not vertex.intree:
                    if current_vertex is None or vertex.distance < current_vertex.distance:
                        current_vertex = vertex

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end=" -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")

if __name__ == "__main__":
    graph_list = ListGraph()
    for vertex1_id, vertex2_id, weight in graf_mst.graf:
        vertex1 = Vertex(vertex1_id)
        vertex2 = Vertex(vertex2_id)
        graph_list.insert_vertex(vertex1)
        graph_list.insert_vertex(vertex2)
        graph_list.insert_edge(vertex1, vertex2, weight)
        graph_list.insert_edge(vertex2, vertex1, weight)
    mst = MST(graph_list)
    printGraph(mst.graph)









