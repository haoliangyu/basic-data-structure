import random

from LinkedList import LinkedList

class ListStack(LinkedList):

    def __init__(self, fromList=None):
        LinkedList.__init__(self, fromList)

    def empty(self):
        return self.tailer.pred_node.pred_node is None

    def push(self, data):
        self.insert_as_last(data)

    def pop(self):
        if self.empty():
            return None

        return self.remove(self.tailer.pred_node)

    def top(self):
        if self.empty():
            return None

        return self.tailer.pred_node

    def permutate(self):
        s = ListStack()
        b = ListStack()

        while self.size() > 0:
            if s.size() == 0:
                s.push(self.pop())
            else:
                coin = random.random()
                if coin < 0.5:
                    s.push(self.pop())
                else:
                    b.push(s.pop())

        while s.size() > 0:
            b.push(s.pop())

        return b

    def get_data(self):
        data = []
        node = self.head.succ_node

        while node.data is not None:
            data.append(node.data)
            node = node.succ_node

        return data

    def equals(self, stack):
        if self.size() != stack.size():
            return False

        this_data = self.get_data()
        stack_data = self.get_data()

        n = self.size()
        i = 0
        while i < n:
            if this_data[i] != stack_data[i]:
                return False
            i += 1

        return True
