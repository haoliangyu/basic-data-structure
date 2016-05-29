from LinkedList import LinkedList

class ListStack(LinkedList):

    def __init__(self, fromList=None):
        LinkedList.__init__(self, fromList)

    def empty(self):
        return self.tailer.pred_node.pred_node is None

    def push(self, data):
        self.tailer.insert_as_pred(data)

    def pop(self):
        if self.empty():
            return None

        return self.remove(self.tailer.pred_node)

    def top(self):
        if self.empty():
            return None

        return self.tailer.pred_node
