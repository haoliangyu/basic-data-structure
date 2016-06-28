import sys

class Vertex(object):

    def __init__(self, data, in_degree=0, out_degree=0, status='UNDISCOVERED', \
                 d_time=-1, f_time=-1, parent=-1, prioity=sys.maxint):
        self.data = data
        self.in_degree = in_degree
        self.out_degree = out_degree
        self.status = status
        self.d_time = d_time
        self.f_time = f_time
        self.parent = parent
        self.prioity = prioity

class Edge(object):

    def __init__(self, data, weight, type='UNDETERMINED'):
        self.data = data
        self.weight = weight
        self.type = type
