from itertools import dropwhile
from typing import List
import math
from copy import deepcopy


class Vertex:
    def __init__(self, key):
        self.key = key
        self.color = None

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.key)


class Edge:
    def __init__(self, weight, is_residual):
        self.weight = weight
        self.is_residual = is_residual
        self.flow = 0
        self.residual = weight

    def __repr__(self):
        return f"[{self.weight} - {self.flow} - {self.residual} - {self.is_residual}]"


class AdjList:
    def __init__(self):
        self.list_of_vertex = []
        self.vertices = {}
        self.neigh_list = {}

    def insertVertex(self, vertex):
        if vertex not in self.list_of_vertex:
            self.list_of_vertex.append(vertex)
            self.vertices[vertex] = len(self.list_of_vertex) - 1
            self.neigh_list[self.vertices[vertex]] = []

    def deleteVertex(self, vertex):
        idx = self.getVertexidx(vertex)
        self.list_of_vertex.pop(idx)
        self.neigh_list.pop(idx)

        for k, v in list(self.neigh_list.items()):
            if k > idx:
                self.neigh_list[k - 1] = self.neigh_list.pop(k)

        for k, v in self.neigh_list.items():
            for i, j in enumerate(v):
                if j[0] == idx:
                    self.neigh_list[k].remove([j[0], j[1]])
                elif j[0] > idx:
                    j[0] -= 1

        for key in dropwhile(lambda k: k != vertex, sorted(self.vertices, key=lambda x: self.vertices[x])):
            self.vertices[key] -= 1
        self.vertices.pop(vertex)

    def insertEdge(self, v1, v2, edge):
        idx1 = self.getVertexidx(v1)
        idx2 = self.getVertexidx(v2)
        self.neigh_list[idx1].append([idx2, edge])

    def deleteEdge(self, v1, v2):
        idx1 = self.getVertexidx(v1)
        idx2 = self.getVertexidx(v2)
        for k, v in enumerate(self.neigh_list[idx1]):
            if v[0] == idx2:
                self.neigh_list[idx1].remove(v)

    def getVertexidx(self, vertex):
        return self.vertices[vertex]

    def getVertex(self, idx):
        return self.list_of_vertex[idx]

    def order(self):
        return len(self.list_of_vertex)

    def get_vert_from_key(self, key):
        for k, v in enumerate(self.list_of_vertex):
            if v.key == key:
                return v
        return False

    def edges(self):
        list_of_edges = []
        for k, v in self.neigh_list.items():
            for elem in v:
                vert1 = self.getVertex(k)
                vert2 = self.getVertex(elem[0])
                list_of_edges.append((vert1.key, vert2.key))
        return list_of_edges

    def size(self):
        return sum(len(v) for v in self.neigh_list.values())

    def neighbours(self, vertex, is_vertex=False):
        if is_vertex:
            return self.neigh_list[self.getVertexidx(vertex)]
        return self.neigh_list[vertex]


def printGraph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end=" -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(g.getVertex(j), f"{w} ", end=": ")
        print()
    print("-------------------")



def initialize_graph(graph: AdjList, vertex_list):            

    for elem in vertex_list:
        v1 = Vertex(elem[0])
        v2 = Vertex(elem[1])
        graph.insertVertex(v1)
        graph.insertVertex(v2)
        graph.insertEdge(v1,v2,Edge(elem[2],is_residual=False))
        edge = Edge(elem[2],is_residual=True)
        edge.residual = 0
        graph.insertEdge(v2,v1,edge)



def bfs(graph:AdjList,start_vertex: Vertex):
    visited = [False for _ in range(graph.order())]
    parrent = {}       
    value = []
    quoue = []

    vertex_idx = graph.getVertexidx(start_vertex)
    quoue.append(vertex_idx)
    visited[vertex_idx] = True
    value.append(start_vertex)
    while quoue:
        elem = quoue.pop(0)
        neigh = graph.neighbours(elem)

        for i in neigh:


            if visited[i[0]] is False and i[1].residual > 0:
                quoue.append(i[0])
                value.append(graph.getVertex(i[0]))
                parrent[graph.getVertex(i[0])] = graph.getVertex(elem)
                visited[i[0]] = True

    return value,parrent




def mini_value(graph: AdjList, start_vertex: Vertex, end_vertex: Vertex, value: List, parent):
    if end_vertex in value:
        act_vertex = end_vertex
        maxi = math.inf

        while act_vertex != start_vertex:
            par_vertex = parent[act_vertex]
            for neighbor_idx, edge in graph.neigh_list[graph.getVertexidx(par_vertex)]:
                if neighbor_idx == graph.getVertexidx(act_vertex) and not edge.is_residual:
                    maxi = min(maxi, edge.residual)
                    break

            act_vertex = par_vertex

        return maxi
    return 0



def augment(graph: AdjList, value: List, minimal, parent):
    act_vertex = value[-1]
    while act_vertex != value[0]:
        par_vertex = parent[act_vertex]

        real_edge = next(edge for neighbor_idx, edge in graph.neigh_list[graph.getVertexidx(par_vertex)]
                          if neighbor_idx == graph.getVertexidx(act_vertex) and not edge.is_residual)
        rest_edge = next(edge for neighbor_idx, edge in graph.neigh_list[graph.getVertexidx(act_vertex)]
                          if neighbor_idx == graph.getVertexidx(par_vertex) and edge.is_residual)

        real_edge.flow += minimal
        real_edge.residual -= minimal
        rest_edge.residual += minimal

        act_vertex = par_vertex


def ford_fulkerson(graph: AdjList, start_vertex: Vertex, end_vertex: Vertex):
    value, parent = bfs(graph, start_vertex)
    if end_vertex in value:
        total_flow = 0
        minimal = mini_value(graph, start_vertex, end_vertex, value, parent)
        total_flow += minimal

        while minimal > 0:
            augment(graph, value, minimal, parent)
            value, parent = bfs(graph, start_vertex)
            minimal = mini_value(graph, start_vertex, end_vertex, value, parent)
            total_flow += minimal

        return total_flow





if __name__ == '__main__':
    graph_0 = AdjList()
    graf_0 = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
    initialize_graph(graph_0,graf_0)

    graph_1 = AdjList()
    graf_1 =  [ ('s', 'a', 16), ('s', 'c', 13), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]
    initialize_graph(graph_1,graf_1)

    graph_2 = AdjList()
    graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    initialize_graph(graph_2,graf_2)

    suma_0 = ford_fulkerson(graph_0,Vertex('s'),Vertex('v'))
    print(f'Flow: {suma_0}')
    print('Graph after operation:')
    printGraph(graph_0)


    suma_1 = ford_fulkerson(graph_1,Vertex('s'),Vertex('t'))
    print(f'Flow: {suma_1}')
    print('Graph after operation:')
    printGraph(graph_1)


    suma_2 = ford_fulkerson(graph_2,Vertex('s'),Vertex('t'))
    print(f'Flow: {suma_2}')
    print('Graph after operation:')
    printGraph(graph_2)
