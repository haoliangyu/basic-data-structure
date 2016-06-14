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

    def __merge(self, lo, mi, hi):
        # prepare left queue
        left_queue = VectorQueue()
        for i in range(lo, mi):
            left_queue.enqueue(self.data[i])

        # prepare right queue
        right_queue = VectorQueue()
        for i in range(mi, hi):
            right_queue.enqueue(self.data[i])

        # result queue
        merged = VectorQueue()

        while not left_queue.empty() or not right_queue.empty():
            if not left_queue.empty() and (right_queue.empty() or left_queue.front() <= right_queue.front()):
                merged.enqueue(left_queue.dequque())

            if not right_queue.empty() and (left_queue.empty() or right_queue.front() < left_queue.front()):
                merged.enqueue(right_queue.dequque)

        self.data = merged.data
