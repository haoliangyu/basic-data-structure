from QuadListNode import QuadListNode

class QuadList(object):

    def __init__(self):
        self.header = QuadListNode()
        self.tailer = QuadListNode()

        self.header.succ_node = self.tailer
        self.tailer.pred_node = self.header

        self.__size = 0

    def empty(self):
        return self.__size == 0

    def clear(self):
        old_size = self.__size

        while not self.empty():
            self.remove(self.header.succ_node)

        return old_size

    def size(self):
        return self.__size

    def first(self):
        return self.header.succ_node

    def last(self):
        return self.tailer.pred_node

    def valid(self, node):
        return (node is not None) and (node is not self.header) and (node is not self.tailer)

    def remove(self, node):
        node.pred_node.succ_node = node.succ_node
        node.succ_node.pred_node = node.pred_node
        self.__size -= 1

        return node.entry

    def insert_after_above(self, entry, p, b=None):
        node = QuadListNode(entry, p, p.succ_node, None, b)

        if p.succ_node is not None:
            p.succ_node.pred_node = node

        p.succ_node = node

        if b is not None:
            b.above_node = node

        return node

    def traverse(self, handler):
        node = self.header.succ_node
        counter = self.__size

        while counter > 0:
            handler(node)
            node = node.succ_node
            counter -= 1
