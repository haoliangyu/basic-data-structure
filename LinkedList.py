class Node(object):

    def __init__(self, data=None, prev_node=None, next_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def insert_as_prev(self, new_data):
        node = Node(new_data, self.prev_node, self)
        self.prev_node.next_node = node
        self.prev_node = node
        return node

    def insert_as_next(self, new_data):
        node = Node(new_data, self, self.next_node)
        self.next_node.prev_node = node
        self.next_node = node
        return node

class LinkedList(object):

    def __init__(self, fromList=None):
        self.head = Node(None, None, None)
        self.tailer = Node(None, None, None)

        self.head.next_node = self.tailer
        self.tailer.prev_node = self.head

        self.__size = 0

        if type(fromList) is list and len(fromList) > 0:
            node = self.head.insert_as_next(fromList[0])
            for i in range(1, len(fromList)):
                node = node.insert_as_next(fromList[i])

    def insert_as_first(self, data):
        self.__size += 1
        return self.head.insert_as_next(data)

    def insert_as_last(self, data):
        self.__size += 1
        return self.tailer.insert_as_prev(data)

    def insert_a(self, node, data):
        self.__size += 1
        return node.insert_as_prev(data)

    def insert_b(self, node, data):
        self.__size += 1
        return node.insert_as_next(data)

    def size(self):
        return self.__size

    def deduplicate(self):
        old_size = self.__size
        node = self.head.next_node
        r = 0
        while node is not None:
            match = self.find(node.data, node, r)
            if match is None:
                r += 1
            else:
                self.remove(match)
            node = node.next_node
        return old_size - self.__size

    def uniquify(self):
        old_size = self.__size
        node = self.head.next_node
        while node.next_node is not None:
            if node.data == node.next_node.data:
                self.remove(node.next_node)
            else:
                node = node.next_node
        return self.__size - old_size

    def search(self, data):
        node = self.head.next_node
        while node.next_node is not None:
            if node.next_node > data:
                return node
            node = node.next_node
        return None

    def find(self, data, n=None, node=None):
        node = node if node is not None else self.tailer
        n = n if n is not None else self.__size
        while n > 0 and node is not None:
            if node.data == data:
                return node
            node = node.prev_node
            n -= 1
        return None

    def disordered(self):
        node = self.head.next_node
        while node.next_node is not None:
            if node.next_node.data < node.data:
                return True
            node = node.prev_node
        return False

    def remove(self, node):
        node.prev_node.next_node = node.next_node
        node.next_node.prev_node = node.prev_node
        self.__size -= 1
        return node.data
