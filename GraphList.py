from GraphElement import Edge, Vertex
from LinkedList import Node
from ListQueue import ListQueue
from ListStack import ListStack

class GraphList(object):

    def __init__(self):
        self.n = 0
        self.e = 0

        self.vertices = []

    def vertex(self, i):
        return self.vertices[i].data['vertex'].data

    def in_degree(self, i):
        return self.vertices[i].data['vertex'].in_degree

    def out_degree(self, i):
        return self.vertices[i].data['vertex'].out_degree

    def d_time(self, i):
        return self.vertices[i].data['vertex'].d_time

    def f_time(self, i):
        return self.vertices[i].data['vertex'].f_time

    def parent(self, i):
        return self.vertices[i].data['vertex'].parent

    def priority(self, i):
        return self.vertices[i].data['vertex'].priority

    def insert_vertex(self, vertex):

        data = {
            'vertex': vertex,
            'edge': None
        }

        vertex_node = Node(data)
        self.vertices.append(vertex_node)

        self.n += 1

    def remove_vertex(self, i):

        to_delete = self.vertices[i].data['vertex']

        for k in range(self.n):
            if k == i:
                continue

            node = self.vertices[k].succ_node
            while node is not None:
                if node.data['vertex'] is to_delete:
                    node.pred_node.succ_node = node.succ_node
                    node.succ_node.pred_node = node.pred_node

                node = node.succ_node

        del self.vertices[i]
        self.n -= 1

    def exists(self, i ,j):
        dest = self.vertices[j].data['vertex']

        node = self.vertices[i].succ_node
        while node is not None:
            if node.data['vertex'] is dest:
                return True
            node = node.succ_node

        return False

    def get_edge(self, i, j):
        dest = self.vertices[j].data['vertex']

        node = self.vertices[i].succ_node
        while node is not None:
            if node.data['vertex'] is dest:
                return node.data['edge']
            node = node.succ_node

        return None

    def type(self, i, j):
        return self.get_edge(i, j).type

    def weight(self, i, j):
        return self.get_edge(i, j).weight

    def edge(self, i, j):
        return self.get_edge(i, j).data

    def insert_edge(self, data, weight, i, j):

        if (self.exists(i, j)):
            return

        start = self.vertices[i].data['vertex']
        start.out_degree += 1

        end = self.vertices[j].data['vertex']
        end.in_degree += 1

        node_data = {
            'vertex': end,
            'edge': Edge(data, weight)
        }
        new_node = Node(node_data, self.vertices[i], self.vertices[i].succ_node)

        if self.vertices[i].succ_node is not None:
            self.vertices[i].succ_node.pred_node = new_node

        self.vertices[i].succ_node = new_node

        self.e += 1

    def remove_edge(self, i, j):
        dest = self.vertices[j].data['vertex']

        node = self.vertices[i].succ_node
        while node is not None:
            if node.data['vertex'] is dest:

                node.pred_node.succ_node = node.succ_node
                node.succ_node.pred_node = node.pred_node

                dest.in_degree -= 1
                self.vertices[i].data['vertex'].out_degree -= 1
                self.e -= 1
                return

            node = node.succ_node

    def first_neighbor(self, i):
        return self.next_neighbor(i, 0)

    def next_neighbor(self, i, j):
        for k in range(j + 1, self.n):
            if self.exists(i, k):
                return k

        return -1

    def reset(self):
        for i in range(self.n):
            vertex = self.vertices[i].data['vertex']
            vertex.status = 'UNDISCOVERED'
            vertex.parent = -1
            vertex.f_time = -1
            vertex.d_time = -1
            vertex.priority = Vertex.init_priority()

            node = self.vertices[i].succ_node
            while node is not None:
                node.data['edge'].type = 'UNDETERMINED'
                node = node.succ_node

    def BFS(self, i, clock):
        queue = ListQueue()

        self.vertices[i].data['vertex'].status = 'DISCOVERED'
        queue.enqueue(i)

        while not queue.empty():
            v = queue.dequeque()
            cur_vertex = self.vertices[v].data['vertex']

            clock += 1
            cur_vertex.d_time = clock

            u = self.first_neighbor(v)
            while u > -1:
                neighbor_vertex = self.vertices[u].data['vertex']
                if neighbor_vertex.status == 'UNDISCOVERED':
                    neighbor_vertex.status = 'DISCOVERED'
                    neighbor_vertex.parent = v
                    queue.enqueue(u)

                    self.get_edge(v, u).type = 'TREE'
                else:
                    self.get_edge(v, u).type = 'CROSS'

                u = self.next_neighbor(v, u)

            cur_vertex.status = 'VISITED'

    def bfs(self):
        self.reset()

        clock = 0
        for i in range(self.n):
            if self.vertices[i].data['vertex'].status == 'UNDISCOVERED':
                self.BFS(i, clock)

    def DFS(self, v, clock):
        clock += 1

        cur_vertex = self.vertices[v].data['vertex']
        cur_vertex.d_time = clock
        cur_vertex.status = 'DISCOVERED'

        u = self.first_neighbor(v)
        while u > -1:
            neighbor_vertex = self.vertices[u].data['vertex']
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
            if self.vertices[i].data['vertex'].status == 'UNDISCOVERED':
                self.DFS(i, clock)

    def TSort(self, v, stack):
        cur_vertex = self.vertices[v].data['vertex']
        cur_vertex.status = 'DISCOVERED'

        u = self.first_neighbor(v)
        while u > -1:
            neighbor_vertex = self.vertices[u].data['vertex']
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
            if self.vertices[i].data['vertex'].status == 'UNDISCOVERED':
                if not self.TSort(i, stack):
                    stack.clear()
                    break

        return stack

    def BCC(self, v, clock, stack):
        clock += 1

        cur_vertex = self.vertices[v].data['vertex']
        cur_vertex.d_time = clock
        cur_vertex.status = 'DISCOVERED'
        stack.push(v)

        u = self.first_neighbor(v)
        while u > -1:
            neighbor_vertex = self.vertices[u].data['vertex']
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
            if self.vertices[i].data['vertex'].status == 'UNDISCOVERED':
                self.BCC(i, clock, stack)
                stack.pop()

    def PFS(self, v, priority_updater):
        cur_vertex = self.vertices[v].data['vertex']
        cur_vertex.priority = 0
        cur_vertex.status = 'VISITED'
        cur_vertex.parent = -1

        while True:
            u = self.first_neighbor(v)
            while u > -1:
                priority_updater(self, v, u)
                u = self.next_neighbor(v, u)

            next_one = None
            priority = Vertex.init_priority()
            u = self.first_neighbor(v)
            while u > -1:
                neighbor_vertex = self.vertices[u].data['vertex']
                if neighbor_vertex.status == 'UNDISCOVERED':
                    if neighbor_vertex.priority < priority:
                        next_one = u
                        priority = neighbor_vertex.priority

                u = self.next_neighbor(v, u)

            next_neighbor = self.vertices[next_one].data['vertex']
            if next_neighbor.status == 'VISITED':
                break

            next_neighbor.status = 'VISITED'
            next_neighbor.parent = v

            self.get_edge(v, u).type = 'TREE'

    def pfs(self, priority_updater):
        self.reset()

        for i in range(self.n):
            if self.vertices[i].data['vertex'].status == 'UNDISCOVERED':
                self.PFS(i, priority_updater)
