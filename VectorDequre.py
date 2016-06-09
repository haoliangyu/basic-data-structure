from Vector import Vector

class VectorQueue(Vector):

    def empty(self):
        return self.size() == 0

    def insert_rear(self, data):
        self.data.append(data)

    def insert_front(self, data):
        self.data.insert(0, data)

    def remove_front(self):
        if not self.empty():
            del self.data[0]

    def remove_rear(self):
        if not self.empty():
            del self.data[-1]

    def front(self):
        return None if self.empty() else self.data[0]

    def rear(self):
        return None if self.empty() else self.data[-1]
