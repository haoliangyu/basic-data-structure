import Vertex from GraphElement

class DisjointSet(object):

    def __init__(self):
        self.set = []

    def add(self, vertex, height=1, parent=None):
        element = {}
        element['parent'] = parent
        element['vertex'] = vertex
        element['height'] = height

        self.set.push(element)

    def find(self, vertex):
        current = [element for element in self.set if element['vertex'] is vertex]

        if len(current) < 1:
            return None

        if len(current) > 1:
            raise Exception('More than two vertex has the same data.')

        current = current[0]
        while current['parent'] is not None:
            current = self.set[current['parent']]

        return current

    def union(self, vertex_dest, vertex_src):
        src = self.find(vertex_src)
        dest = self.find(vertex_dest)

        if src['height'] < dest['height']:
            src['parent'] = self.set.index(dest)
        else if src['height'] > dest['height']:
            dest['parent'] = self.set.index(src)
        else:
            dest['parent'] = self.set.index(src)
            dest['height'] += 1

        return dest
