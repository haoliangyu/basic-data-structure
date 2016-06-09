from Vector import Vector

class VectorQueue(Vector):

    def empty(self):
        return self.size() == 0

    def enqueue(self, data):
        self.data.append(data)

    def dequque(self):
        if not self.empty():
            del self.data[0]

    def front(self):
        return None if self.empty() else self.data[0]
