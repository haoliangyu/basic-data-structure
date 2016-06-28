from GraphElement import Edge

class GraphMatrix(object):

    def __init__(self):
        self.n = 0
        self.e = 0

        self.edges = []
        self.vertices = []

    def vector(self, i):
        return self.vertices[i].data

    def in_degree(self, i):
        return self.vertices[i].in_degree

    def out_degree(self, i):
        return self.vertices[i].out_degree

    def d_time(self, i):
        return self.vertices[i].d_time

    def f_time(self, i):
        return self.vertices[i].f_time

    def parent(self, i):
        return self.vertices[i].parent

    def priority(self, i):
        return self.vertices[i].priority

    def insert_vertex(self, vertex):
        for row in self.edges:
            row.append(None)

        self.n += 1
        self.edges.append([None] * self.n)
        self.vertices.append(vertex)

    def remove_vertex(self, i):
        del self.edges[i]

        for row in self.edges:
            del row[i]

        vertex = self.vertices[i]
        del self.vertices[i]

        self.n -= 1

        return vertex

    def exists(self, i, j):
        return 0 <= i < self.n and 0 <= j < self.n and self.edges[i][j] is not None

    def type(self, i, j):
        return self.edges[i][j].type

    def edge(self, i, j):
        return self.edges[i][j].data

    def weight(self, i, j):
        return self.edges[i][j].weight

    def insert_edge(self, data, weight, i, j):
        if (self.exists(i, j)):
            return

        self.edges[i][j] = Edge(data, weight)
        self.e += 1
        self.vertices[i].out_degree += 1
        self.vertices[j].in_degree += 1

    def remove_edge(self, i, j):
        edge = self.edges[i][j]

        self.edges[i][j] = None
        self.vertices[i].out_degree -= 1
        self.vertices[j].in_degree -= 1

        return edge
