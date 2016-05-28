class Stack(object):

    def __init__(self, fromList=None):
        self.data = [] if fromList is None else fromList

    def size(self):
        return len(self.data)

    def empty(self):
        return self.size() == 0

    def push(self, data):
        self.data.push(data)

    def pop(self):
        return self.pop()

    def top(self):
        return self.data[-1]
