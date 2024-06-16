from typing import List, Tuple
from copy import deepcopy

class Vertex:
    def __init__(self, key) -> None:
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return f'{self.key}'
    

class Matrix:
    def __init__(self, m, val = 0):
        if isinstance(m, Tuple):
            rows, cols = m
            self.matrix = [[val for _ in range(cols)] for _ in range(rows)]
        else:
            self.matrix = m
    
    def size(self):
        rows, cols = len(self.matrix), len(self.matrix[0])
        return (rows, cols)

    def __add__(self, A):
        if self.size() != A.size():
            return 'Wrong size!'
        else:
            ans = [[i+j for i,j in zip(x, y)] for x,y in zip(self.matrix, A)] 

            add_result = Matrix(ans)
        return add_result

    def __mul__(self, A):
        if self.size()[1] != A.size()[0]:
            return 'Wrong size!'
        else:
            rows = self.size()[0]
            cols = A.size()[1]
            ans = [[0 for _ in range(cols)] for _ in range(rows)]

            for i in range(rows):
                for j in range(cols):
                    for k in range(A.size()[0]):
                        ans[i][j] += self.matrix[i][k] * A[k][j]
            
            multiply_result = Matrix(ans)
            
        return multiply_result

    def __getitem__(self, item):
        return self.matrix[item]

    def __str__(self):
        rows, cols = self.size()
        result = ""

        for i in range(rows):
            result += "| "
            for j in range(cols):
                result += str(self.matrix[i][j]) + " "
            result += "|\n"

        return result
    
    def __eq__(self, other) -> bool:
        for row in range(other):
            if self.matrix[row] != other.matrix[row]:
                return False
            
        return True


def transpose(A):
    matrix_transposed = list(zip(*A))
    result = Matrix(matrix_transposed)

    return result
    
    
class AdjacencyMatrix:
    def __init__(self):
        self.matrix = []
        self.v_list = []

    def is_empty(self):
        return len(self.matrix) == 0

    def insert_vertex(self, vertex):
        if vertex not in self.v_list:
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
    
def ullmann(current_used, current_row, M, count=0):
    count = count
    start_list = [False for _ in range(M.size()[1])]
    if current_row == M.size()[0]:

        print(M)
        return
    
    rows, cols = M.size()

    for col in range(cols):
        if not current_used[col]:
            current_used[col] = True

            for j in range(cols):
                M[current_row][j] = 0
            M[current_row][col] = 1
            next_row = current_row + 1
            count += 1
            ullmann(current_used.copy(), next_row, M, count) 
            current_used[col] = False  

    return count



          
def printGraph(g):
    print("------GRAPH------")
    for v in g.v_list:
        print(v, end=" -> ")
        for n, w in g.neighbours(v):
            print(n, w, end="; ")
        print()
    print("-------------------")
    
if __name__ == "__main__":
    graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
    graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]

    G_G = AdjacencyMatrix()
    for v in graph_G:
        v1 = Vertex(v[0])
        v2 = Vertex(v[1])
        G_G.insert_vertex(v1)
        G_G.insert_vertex(v2)
        G_G.insert_edge(v1, v2, v[2])


    G_P = AdjacencyMatrix()
    for v in graph_P:
        v1 = Vertex(v[0])
        v2 = Vertex(v[1])
        G_P.insert_vertex(v1)
        G_P.insert_vertex(v2)
        G_P.insert_edge(v1, v2, v[2])


    printGraph(G_G)
    printGraph(G_P)

    M = Matrix((3, 6))
    list_M = [False for x in range(6)]
    print(M)
    ullmann(list_M, 0, M)










































# from typing import List, Tuple
# from copy import deepcopy

# class Vertex:
#     def __init__(self, key) -> None:
#         self.key = key

#     def __eq__(self, other):
#         return self.key == other.key

#     def __hash__(self):
#         return hash(self.key)

#     def __str__(self):
#         return f'{self.key}'
    

# class Matrix:
#     def __init__(self, m, val = 0):
#         if isinstance(m, Tuple):
#             rows, cols = m
#             self.matrix = [[val for _ in range(cols)] for _ in range(rows)]
#         else:
#             self.matrix = m
    
#     def size(self):
#         rows, cols = len(self.matrix), len(self.matrix[0])
#         return (rows, cols)

#     def __add__(self, A):
#         if self.size() != A.size():
#             return 'Wrong size!'
#         else:
#             ans = [[i+j for i,j in zip(self.matrix, A)] for self.matrix, A in zip(self.matrix, A)]

#             add_result = Matrix(ans)
#         return add_result

#     def __mul__(self, A):
#         if self.size()[0] != A.size()[1] and self.size()[1] != A.size()[0]:
#             return 'Wrong size!'
#         else:
#             rows = self.size()[0]
#             cols = A.size()[1]
#             ans = [[0 for _ in range(cols)] for _ in range(rows)]

#             for i in range(rows):
#                 for j in range(cols):
#                     for k in range(A.size()[0]):
#                         ans[i][j] += self.matrix[i][k] * A[k][j]
            
#             multiply_result = Matrix(ans)
            
#         return multiply_result

#     def __getitem__(self, item):
#         return self.matrix[item]

#     def __str__(self):
#         rows, cols = self.size()
#         result = ""

#         for i in range(rows):
#             result += "| "
#             for j in range(cols):
#                 result += str(self.matrix[i][j]) + " "
#             result += "|\n"

#         return result
    
#     def __eq__(self, other) -> bool:
#         for row in range(other):
#             if self.matrix[row] != other.matrix[row]:
#                 return False
            
#         return True


# def transpose(A):
#     matrix_transposed = list(zip(*A))
#     result = Matrix(matrix_transposed)

#     return result
    
    
# class AdjacencyMatrix:
#     def __init__(self):
#         self.matrix = []
#         self.v_list = []

#     def is_empty(self):
#         return len(self.matrix) == 0

#     def insert_vertex(self, vertex):
#         if vertex not in self.v_list:
#             self.v_list.append(vertex)

#             for row in self.matrix:
#                 row.append(0)

#             self.matrix.append([0] * (len(self.v_list)+1))

#     def insert_edge(self, vertex1, vertex2, edge=1):
#         idx1 = self.v_list.index(vertex1)
#         idx2 = self.v_list.index(vertex2)
#         self.matrix[idx1][idx2] = edge
#         self.matrix[idx2][idx1] = edge

#     def delete_vertex(self, vertex):
#         idx = self.v_list.index(vertex)
#         self.v_list.remove(vertex)
#         self.matrix.pop(idx)
#         for row in self.matrix:
#             row.pop(idx)

#     def delete_edge(self, vertex1, vertex2):
#         idx1 = self.v_list.index(vertex1)
#         idx2 = self.v_list.index(vertex2)
#         self.matrix[idx1][idx2] = 0
#         self.matrix[idx2][idx1] = 0

#     def get_vertex(self, vertex_id):
#         idx = self.v_list.index(vertex_id)
#         return self.v_list[idx]

#     def vertices(self):
#         return self.v_list

#     def neighbours(self, vertex_id):
#         vertex_id = self.v_list.index(vertex_id)
#         return [
#             (self.v_list[i], self.matrix[vertex_id][i])
#             for i in range(len(self.v_list))
#             if self.matrix[vertex_id][i] != 0
#         ]
    
# def ullmann(current_used, current_row, M):
#     if current_row == M.size()[0]:
#         print(M)
#         return
    
#     rows, cols = M.size()

#     for col in range(cols):
#         if not current_used[col]:
#             current_used[col] = True

#             for j in range(cols):
#                 M[current_row][j] = 0
#             M[current_row][col] = 1
#             next_row = current_row + 1
#             count = ullmann(current_used.copy(), next_row, M) 
#             current_used[col] = False  

          
# def printGraph(g):
#     print("------GRAPH------")
#     for v in g.v_list:
#         print(v, end=" -> ")
#         for n, w in g.neighbours(v):
#             print(n, w, end="; ")
#         print()
#     print("-------------------")
    
# if __name__ == "__main__":
#     graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
#     graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]

#     G_G = AdjacencyMatrix()
#     for v in graph_G:
#         v1 = Vertex(v[0])
#         v2 = Vertex(v[1])
#         G_G.insert_vertex(v1)
#         G_G.insert_vertex(v2)
#         G_G.insert_edge(v1, v2, v[2])


#     G_P = AdjacencyMatrix()
#     for v in graph_P:
#         v1 = Vertex(v[0])
#         v2 = Vertex(v[1])
#         G_P.insert_vertex(v1)
#         G_P.insert_vertex(v2)
#         G_P.insert_edge(v1, v2, v[2])


#     printGraph(G_G)
#     printGraph(G_P)

#     M = Matrix((3, 6))
#     list_M = [False for x in range(6)]
#     print(M)
#     ullmann(list_M, 0, M)
