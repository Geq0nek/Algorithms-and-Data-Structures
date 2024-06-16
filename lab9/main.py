import math

class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.key)


class Edge:
    def __init__(self, weight):
        self.weight = weight


class AdjacencyList:
    def __init__(self):
        self.vertices = {}
        self.adjList = {}

    def insertVertex(self, vertex):
        self.vertices[vertex] = len(self.vertices)
        self.adjList[vertex] = []

    def deleteVertex(self, vertex):
        idx = self.vertices.pop(vertex)
        self.adjList.pop(vertex)
        for adj_vertex in self.adjList.values():
            for i, (v, w) in enumerate(adj_vertex):
                if v == idx:
                    adj_vertex.pop(i)
                elif v > idx:
                    adj_vertex[i] = (v - 1, w)

    def insertEdge(self, vertex1, vertex2, edge):
        self.adjList[vertex1].append((vertex2, edge.weight))
        self.adjList[vertex2].append((vertex1, edge.weight))

    def deleteEdge(self, vertex1, vertex2):
        self.adjList[vertex1] = [(v, w) for v, w in self.adjList[vertex1] if v != vertex2]
        self.adjList[vertex2] = [(v, w) for v, w in self.adjList[vertex2] if v != vertex1]

    def order(self):
        return len(self.vertices)

    def getVertex(self, key):
        return key

    def edges(self):
        edges = []
        for v, neighbors in self.adjList.items():
            for neighbor, weight in neighbors:
                edges.append((v, neighbor))
        return edges

    def size(self):
        return sum(len(neighbors) for neighbors in self.adjList.values())

    def neighbors(self, vertex):
        return self.adjList[vertex]


def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices:
        print(v, end=" -> ")
        for neighbor, weight in g.adjList[v]:
            print(neighbor, weight, end="; ")
        print()
    print("-------------------")


def prim_mst(G, s):
    intree = {vertex: 0 for vertex in G.vertices}
    distance = {vertex: math.inf for vertex in G.vertices}
    parent = {vertex: None for vertex in G.vertices}

    mst_tree = AdjacencyList()
    for vertex in G.vertices:
        mst_tree.insertVertex(vertex)

    v = s
    sum_tree = 0

    while True:
        intree[v] = 1
        for neighbor, weight in G.neighbors(v):
            if weight < distance[neighbor] and intree[neighbor] == 0:
                distance[neighbor] = weight
                parent[neighbor] = v

        min_dist = math.inf
        for vertex in G.vertices:
            if intree[vertex] == 0 and distance[vertex] < min_dist:
                min_dist = distance[vertex]
                v = vertex

        if intree[v] == 1:
            break

        mst_tree.insertEdge(v, parent[v], Edge(min_dist))
        sum_tree += min_dist

    return mst_tree, sum_tree


if __name__ == '__main__':
    graf = [('A', 'B', 4), ('A', 'C', 1), ('A', 'D', 4),
            ('B', 'E', 9), ('B', 'F', 9), ('B', 'G', 7), ('B', 'C', 5),
            ('C', 'G', 9), ('C', 'D', 3),
            ('D', 'G', 10), ('D', 'J', 18),
            ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
            ('F', 'H', 2), ('F', 'G', 8),
            ('G', 'H', 9), ('G', 'J', 8),
            ('H', 'I', 3), ('H', 'J', 9),
            ('I', 'J', 9)
            ]

    G = AdjacencyList()

    for v1, v2, weight in graf:
        if v1 not in G.vertices:
            G.insertVertex(v1)
        if v2 not in G.vertices:
            G.insertVertex(v2)

        G.insertEdge(v1, v2, Edge(weight))

    mst, sum_mst = prim_mst(G, 'A')
    printGraph(mst)
    print(f'MST size: {sum_mst}')
