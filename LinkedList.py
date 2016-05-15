import sys

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

    def __str__(self):
        return str(self.data)

class LinkedList(object):

    def __init__(self, fromList=None):
        self.head = Node(None, None, None)
        self.tailer = Node(None, None, None)

        self.head.next_node = self.tailer
        self.tailer.prev_node = self.head

        self.__size = 0

        if type(fromList) is list and len(fromList) > 0:
            node = self.head.insert_as_next(fromList[0])
            self.__size = len(fromList)
            for i in range(1, len(fromList)):
                node = node.insert_as_next(fromList[i])

    def __str__(self):
        data_list = []
        node = self.head.next_node

        while node.data is not None:
            data_list.append(node.data)
            node = node.next_node

        return ', '.join(map(str, data_list))

    def insert_as_first(self, data):
        self.__size += 1
        return self.head.insert_as_next(data)

    def insert_as_last(self, data):
        self.__size += 1
        return self.tailer.insert_as_prev(data)

    def insert_b(self, node, data):
        self.__size += 1
        return node.insert_as_prev(data)

    def insert_a(self, node, data):
        self.__size += 1
        return node.insert_as_next(data)

    def size(self):
        return self.__size

    def deduplicate(self):
        if self.__size < 2: return False
        old_size = self.__size
        node = self.head.next_node
        r = 0
        while node.data is not None:
            match = self.find(node.data, r, node)
            if match is None:
                r += 1
            elif match.data == node.data:
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

    def search(self, data, n=None, node=None):
        node = node if node is not None else self.tailer
        n = n if n is not None else self.__size
        while n > 0 and node.prev_node.data is not None:
            if node.prev_node.data <= data:
                return node.prev_node
            node = node.prev_node
            n -= 1
        return None

    def find(self, data, n=None, node=None):
        node = node if node is not None else self.tailer
        n = n if n is not None else self.__size
        while n > 0 and node.prev_node.data is not None:
            if node.prev_node.data <= data:
                return node.prev_node
            node = node.prev_node
            n -= 1
        return None

    def disordered(self):
        if self.__size < 2: return False
        node = self.head.next_node
        while node.next_node.data is not None:
            if node.next_node.data < node.data:
                return True
            node = node.next_node
        return False

    def remove(self, node):
        node.prev_node.next_node = node.next_node
        node.next_node.prev_node = node.prev_node
        self.__size -= 1
        return node

    def sort(self, method):
        if method == 'insert_sort':
            self.insert_sort()
        elif method == 'selection_sort':
            self.selection_sort()
        elif method == 'merge_sort':
            self.merge_sort(self.head.next_node, self.__size)
        else:
            return

    def insert_sort(self):
        if self.__size < 2: return
        node = self.head.next_node
        r = 0
        while r < self.__size:
            match = self.find(node.data, r, node)
            self.insert_a(self.head if match is None else match, node.data)
            node = self.remove(node).next_node
            r += 1

    def selection_sort(self):
        if self.__size < 2:
            return

        def find_max(r):
            max_data = -sys.maxint - 1
            max_node = None
            node = self.head.next_node
            n = 0
            while n < r:
                if node.data > max_data:
                    max_node = node
                    max_data = node.data
                node = node.next_node
                n += 1
            return max_node

        r = self.__size
        node = self.tailer
        while r > 1:
            match = find_max(r)
            self.insert_b(node, self.remove(match).data)
            node = node.prev_node
            r -= 1

    def __merge(self, node_p, n, node_q, m):
        start = node_p.prev_node

        while m > 0:
            if  n > 0 and node_p.data <= node_q.data:
                if node_p.next_node is node_q:
                    break
                node_p = node_p.next_node
                n -= 1
            else:
                self.insert_b(node_p, self.remove(node_q).data)
                node_q = node_q.next_node
                m -= 1

        node_p = start.next_node

    def merge_sort(self, node_p, n):
        if n < 2:
            return
        middle = n >> 1

        node_q = node_p
        for i in range(middle):
            node_q = node_q.next_node

        self.merge_sort(node_p, middle)
        self.merge_sort(node_q, n - middle)

        self.__merge(node_p, middle, node_q, n - middle)
