import polska
from collections import deque

class Vertex:
    def __init__(self, key) -> None:
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return f'{self.key}'

class AdjacencyList:
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
        if vertex in self.adjList:
            del self.adjList[vertex]

            for k in self.adjList:
                if vertex in self.adjList[k]:
                    del self.adjList[k][vertex]

    def delete_edge(self, vertex1, vertex2):
        if vertex1 in self.adjList and vertex2 in self.adjList[vertex1]:
            self.adjList[vertex1].pop(vertex2, None)

        if vertex2 in self.adjList and vertex1 in self.adjList[vertex2]:
            self.adjList[vertex2].pop(vertex1, None)

    def neighbours(self, vertex_id):
        if vertex_id in self.dict:
            return self.dict[vertex_id].items()

    def get_vertex(self, vertex_id):
        return vertex_id

    def vertices(self):
        return self.dict.keys()


def DFS(G, v):
    visited = set()
    stack = [v]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            yield vertex
            visited.add(vertex)
            stack.extend(x for x, _ in G.neighbours(vertex) if x not in visited)

def BFS(G, v):
    visited = set()
    queue = deque([v])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            yield vertex
            visited.add(vertex)
            queue.extend(x for x, _ in G.neighbours(vertex) if x not in visited)

def color_graph(G, type):
    colors = {}
    count = 0

    search_algorithm = DFS if type == 'DFS' else BFS
    start_vertex = next(iter(G.vertices()))

    for vertex in search_algorithm(G, start_vertex):
        neighbour_colors = {colors.get(neighbour) for neighbour, _ in G.neighbours(vertex)}
        available_colors = {i for i in range(count + 1)} - neighbour_colors
        if not available_colors:
            count += 1
            colors[vertex] = count
        else:
            colors[vertex] = min(available_colors)

    return [(vertex, colors[vertex]) for vertex in G.vertices()]

graph = AdjacencyList()
for vertex in polska.graf:
    graph.insert_edge(vertex[0], vertex[1], 0)

# colored_graph_DFS = color_graph(graph, 'DFS')
colored_graph_BFS = color_graph(graph, 'BFS')

# polska.draw_map(graph, colored_graph_DFS)
polska.draw_map(graph, colored_graph_BFS)