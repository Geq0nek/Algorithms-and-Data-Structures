import polska

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
    def __init__(self) -> None:
        self.adjList = {}
    
    def is_empty(self):
        return len(self.adjList.keys()) == 0

    def insert_vertex(self, vertex):
        if vertex not in self.adjList.keys():
            self.adjList[vertex] = {}

    def insert_edge(self, vertex1, vertex2, edge=None):
        self.insert_vertex(vertex1)
        self.insert_vertex(vertex2)
        self.adjList[vertex1][vertex2] = edge
        self.adjList[vertex1][vertex2] = edge

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
                

    def get_vertex(self, vertex_id):
        return vertex_id
    
    def vertices(self):
        return self.adjList.keys()
        
    def neighbours(self, vertex_id):
        if vertex_id in self.adjList:
            return self.adjList[vertex_id].items()
        
class AdjacencyMatrix:
    def __init__(self):
        self.matrix = []
        self.v_list = []

    def is_empty(self):
        return len(self.matrix) == 0

    def insert_vertex(self, vertex):
        self.v_list.append(vertex)

        for row in self.matrix:
            row.append(0)

        self.matrix.append([0] * (len(self.v_list)+1))

    def insert_edge(self, vertex1, vertex2, edge=1):
        idx1 = self.v_list.index(vertex1)
        idx2 = self.v_list.index(vertex2)
        self.matrix[idx1][idx2] = edge
        self.matrix[idx2][idx1] = edge

    def delete_vertex(self, vertex):
        idx = self.v_list.index(vertex)
        self.v_list.remove(vertex)
        self.matrix.pop(idx)
        for row in self.matrix:
            row.pop(idx)

    def delete_edge(self, vertex1, vertex2):
        idx1 = self.v_list.index(vertex1)
        idx2 = self.v_list.index(vertex2)
        self.matrix[idx1][idx2] = 0
        self.matrix[idx2][idx1] = 0

    def get_vertex(self, vertex_id):
        idx = self.v_list.index(vertex_id)
        return self.v_list[idx]

    def vertices(self):
        return self.v_list

    def neighbours(self, vertex_id):
        vertex_id = self.v_list.index(vertex_id)
        return [
            (self.v_list[i], self.matrix[vertex_id][i])
            for i in range(len(self.v_list))
            if self.matrix[vertex_id][i] != 0
        ]
    
if __name__ == "__main__":
    adjacency_list_graph = AdjacencyList()
    for vertex in polska.graf:
        adjacency_list_graph.insert_edge(vertex[0], vertex[1], 1)
    adjacency_list_graph.delete_vertex("K")
    adjacency_list_graph.delete_edge("E", "W")   

    
    polska.draw_map(adjacency_list_graph)

    # adjacency_matrix_graph = AdjacencyMatrix()
    # for vertexs in polska.graf:
    #     adjacency_matrix_graph.insert_vertex(vertexs[0])
    # for edges in polska.graf:
    #     adjacency_matrix_graph.insert_edge(edges[0], edges[1], 1)

    # adjacency_matrix_graph.delete_vertex('K')
    # adjacency_matrix_graph.delete_edge('E', 'W')

    # for vertex_data in polska.polska:
    #     adjacency_matrix_graph.insert_vertex(vertex_data[2])

    # polska.draw_map(adjacency_matrix_graph)
        
        
