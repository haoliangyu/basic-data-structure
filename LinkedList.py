import sys

class Node(object):

    def __init__(self, data=None, pred_node=None, succ_node=None):
        self.data = data
        self.succ_node = succ_node
        self.pred_node = pred_node

    def insert_as_pred(self, new_data):
        node = Node(new_data, self.pred_node, self)
        self.pred_node.succ_node = node
        self.pred_node = node
        return node

    def insert_as_succ(self, new_data):
        node = Node(new_data, self, self.succ_node)
        self.succ_node.pred_node = node
        self.succ_node = node
        return node

    def __str__(self):
        return str(self.data)

class LinkedList(object):

    def __init__(self, fromList=None):
        self.head = Node(None, None, None)
        self.tailer = Node(None, None, None)

        self.head.succ_node = self.tailer
        self.tailer.pred_node = self.head

        self.__size = 0

        if type(fromList) is list and len(fromList) > 0:
            node = self.head.insert_as_succ(fromList[0])
            self.__size = len(fromList)
            for i in range(1, len(fromList)):
                node = node.insert_as_succ(fromList[i])

    def __str__(self):
        data_list = []
        node = self.head.succ_node

        while node.data is not None:
            data_list.append(node.data)
            node = node.succ_node

        return ', '.join(map(str, data_list))

    def insert_as_first(self, data):
        self.__size += 1
        return self.head.insert_as_succ(data)

    def insert_as_last(self, data):
        self.__size += 1
        return self.tailer.insert_as_pred(data)

    def insert_b(self, node, data):
        self.__size += 1
        return node.insert_as_pred(data)

    def insert_a(self, node, data):
        self.__size += 1
        return node.insert_as_succ(data)

    def size(self):
        return self.__size

    def deduplicate(self):
        if self.__size < 2: return False
        old_size = self.__size
        node = self.head.succ_node
        r = 0
        while node.data is not None:
            match = self.find(node.data, r, node)
            if match is None:
                r += 1
            elif match.data == node.data:
                self.remove(match)
            node = node.succ_node
        return old_size - self.__size

    def uniquify(self):
        old_size = self.__size
        node = self.head.succ_node
        while node.succ_node is not None:
            if node.data == node.succ_node.data:
                self.remove(node.succ_node)
            else:
                node = node.succ_node
        return self.__size - old_size

    def search(self, data, n=None, node=None):
        node = node if node is not None else self.tailer
        n = n if n is not None else self.__size
        while n > 0 and node.pred_node.data is not None:
            if node.pred_node.data <= data:
                return node.pred_node
            node = node.pred_node
            n -= 1
        return None

    def find(self, data, n=None, node=None):
        node = node if node is not None else self.tailer
        n = n if n is not None else self.__size
        while n > 0 and node.pred_node.data is not None:
            if node.pred_node.data == data:
                return node.pred_node
            node = node.pred_node
            n -= 1
        return None

    def disordered(self):
        if self.__size < 2: return False
        node = self.head.succ_node
        while node.succ_node.data is not None:
            if node.succ_node.data < node.data:
                return True
            node = node.succ_node
        return False

    def remove(self, node):
        node.pred_node.succ_node = node.succ_node
        node.succ_node.pred_node = node.pred_node
        self.__size -= 1
        return node.data

    def sort(self, method):
        if method == 'insert_sort':
            self.insert_sort()
        elif method == 'selection_sort':
            self.selection_sort()
        elif method == 'merge_sort':
            self.merge_sort(self.head.succ_node, self.__size)
        else:
            return

    def insert_sort(self):
        if self.__size < 2: return
        node = self.head.succ_node
        r = 0
        while r < self.__size:
            match = self.search(node.data, r, node)
            self.insert_a(self.head if match is None else match, node.data)
            self.remove(node)
            node = node.succ_node
            r += 1

    def selection_sort(self):
        if self.__size < 2:
            return

        def find_max(r):
            max_data = -sys.maxint - 1
            max_node = None
            node = self.head.succ_node
            n = 0
            while n < r:
                if node.data > max_data:
                    max_node = node
                    max_data = node.data
                node = node.succ_node
                n += 1
            return max_node

        r = self.__size
        node = self.tailer
        while r > 1:
            match = find_max(r)
            self.insert_b(node, self.remove(match))
            node = node.pred_node
            r -= 1

    def __merge(self, node_p, n, node_q, m):
        start = node_p.pred_node

        while m > 0:
            if  n > 0 and node_p.data <= node_q.data:
                if node_p.succ_node is node_q:
                    break
                node_p = node_p.succ_node
                n -= 1
            else:
                self.insert_b(node_p, self.remove(node_q))
                node_q = node_q.succ_node
                m -= 1

        node_p = start.succ_node

    def merge_sort(self, node_p, n):
        if n < 2:
            return
        middle = n >> 1

        node_q = node_p
        for i in range(middle):
            node_q = node_q.succ_node

        self.merge_sort(node_p, middle)
        self.merge_sort(node_q, n - middle)

        self.__merge(node_p, middle, node_q, n - middle)
