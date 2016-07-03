from LinkedList import LinkedList

class ListQueue(LinkedList):

    def empty(self):
        return self.size() == 0

    def enqueue(self, data):
        self.insert_as_last(data)

    def dequeque(self):
        if not self.empty():
            return self.remove(self.head.succ_node)

        return None

    def front(self):
        return None if self.empty() else self.head.succ_node.data
