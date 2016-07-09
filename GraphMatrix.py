from GraphElement import Edge, Vertex
from ListQueue import ListQueue
from ListStack import ListStack

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

    def get_edge(self, i, j):
        return self.edges[i][j]

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

    def first_neighbor(self, i):
        return self.next_neighbor(i, 0)

    def next_neighbor(self, i, j):
        for k in range(j + 1, self.n):
            if self.exists(i, k):
                return k

        return -1

    def reset(self):
        for i in range(self.n):
            vertex = self.vertices[i]
            vertex.status = 'UNDISCOVERED'
            vertex.parent = -1
            vertex.f_time = -1
            vertex.d_time = -1
            vertex.priority = Vertex.init_priority()

            for j in range(self.n):
                if self.exists(i, j):
                    self.edges[i][j].type = 'UNDETERMINED'

    def BFS(self, i, clock):
        queue = ListQueue()

        self.vertices[i].status = 'DISCOVERED'
        queue.enqueue(i)

        while not queue.empty():
            v = queue.dequeque()

            clock += 1
            self.vertices[v].d_time = clock

            u = self.first_neighbor(v)
            while u > -1:
                if self.vertices[u].status == 'UNDISCOVERED':
                    self.vertices[u].status = 'DISCOVERED'
                    self.get_edge(v, u).type = 'TREE'
                    self.vertices[u].parent = v
                    queue.enqueue(u)
                else:
                    self.get_edge(v, u).type = 'CROSS'
                u = self.next_neighbor(v, u)

            self.vertices[v].status = 'VISITED'

    def bfs(self):
        self.reset()

        clock = 0
        for i in range(self.n):
            if self.vertices[i].status == 'UNDISCOVERED':
                self.BFS(i, clock)

    def DFS(self, v, clock):
        clock += 1

        cur_vertex = self.vertices[v]
        cur_vertex.d_time = clock
        cur_vertex.status = 'DISCOVERED'

        u = self.first_neighbor(v)
        while u > -1:
            neighbor_vertex = self.vertices[u]
            if neighbor_vertex.status == 'UNDISCOVERED':
                neighbor_vertex.parent = v
                self.get_edge(v, u).type = 'TREE'
                self.DFS(u, clock)
            elif neighbor_vertex.status == 'DISCOVERED':
                self.get_edge(v, u).type = 'BACKWARD'
            else:
                self.get_edge(v, u).type = 'FORWARD' if cur_vertex.d_time < neighbor_vertex.d_time else 'CROSS'

            u = self.next_neighbor(v, u)

        clock += 1

        cur_vertex.status = 'VISITED'
        cur_vertex.f_time = clock

    def dfs(self):
        self.reset()
        clock = 0

        for i in range(self.n):
            if self.vertices[i].status == 'UNDISCOVERED':
                self.DFS(i, clock)

    def TSort(self, v, stack):
        cur_vertex = self.vertices[v]
        cur_vertex.status = 'DISCOVERED'

        u = self.first_neighbor(v)
        while u > -1:
            neighbor_vertex = self.vertices[u]
            if neighbor_vertex.status == 'UNDISCOVERED':
                if not self.TSort(u, stack):
                    return False
            elif neighbor_vertex.status == 'DISCOVERED':
                return False

            u = self.next_neighbor(v, u)

        stack.push(cur_vertex)
        return True

    def tsort(self):
        self.reset()

        stack = ListStack()
        for i in range(self.n):
            if self.vertices[i].status == 'UNDISCOVERED':
                if not self.TSort(i, stack):
                    stack.clear()
                    break

        return stack

    def _hca(self, vertex):
        return vertex.f_time

    def BCC(self, v, clock, stack):
        clock += 1

        cur_vertex = self.vertices[v]
        cur_vertex.d_time = clock
        cur_vertex.status = 'DISCOVERED'
        stack.push(v)

        u = self.first_neighbor(v)
        while u > -1:
            neighbor_vertex = self.vertices[u]
            if neighbor_vertex.status == 'UNDISCOVERED':
                neighbor_vertex.parent = v
                self.get_edge(v, u).type = 'TREE'
                self.BCC(u, clock, stack)

                if neighbor_vertex.f_time < cur_vertex.d_time:
                    cur_vertex.f_time = neighbor_vertex.f_time if neighbor_vertex.f_time < cur_vertex.f_time else \
                                             cur_vertex.f_time
                else:
                    temp = stack.pop()
                    while temp != v:
                        temp = stack.pop()
                    stack.push(v)
            elif neighbor_vertex.status == 'DISCOVERED':
                self.get_edge(v, u).type = 'BACKWARD'
                if cur_vertex.parent != u:
                    cur_vertex.f_time = neighbor_vertex.f_time if neighbor_vertex.f_time < cur_vertex.f_time else \
                                             cur_vertex.f_time

            u = self.next_neighbor(v, u)
        cur_vertex.status = 'VISITED'

    def bcc(self):
        self.reset()
        clock = 0
        stack = ListStack()

        for i in range(self.n):
            if self.vertices[i].status == 'UNDISCOVERED':
                self.BCC(i, clock, stack)
                stack.pop()
