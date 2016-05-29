from Vector import Vector

class VectorStack(Vector):

    def __init__(self, fromList=None):
        Vector.__init__(self, fromList)

    def empty(self):
        return self.size() == 0

    def push(self, data):
        self.data.append(data)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]
