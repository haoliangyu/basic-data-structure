from LinkedList import LinkedList

class ListQueue(LinkedList):

    def empty(self):
        return self.size() == 0

    def insert_front(self, data):
        self.insert_as_first(data)

    def insert_rear(self, data):
        self.insert_as_last(data)

    def remove_front(self):
        if not self.empty():
            return self.remove(self.head.succ_node)

    def remove_rear(self):
        if not self.empty():
            return self.remove(self.tailer.pred_node)

    def front(self):
        return None if self.empty() else self.head.succ_node.data

    def rear(self):
        return None if self.empty() else self.tailer.pred_node.data
