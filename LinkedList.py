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

    def is_header(self):
        return self.pred_node is None

    def is_tailer(self):
        return self.succ_node is None

    def is_first(self):
        return False if self.is_header() else self.pred_node.is_header()

    def __str__(self):
        return str(self.data)

class LinkedList(object):

    def __init__(self, fromList=None):
        self.header = Node(None, None, None)
        self.tailer = Node(None, None, None)

        self.header.succ_node = self.tailer
        self.tailer.pred_node = self.header

        self.__size = 0

        if type(fromList) is list and len(fromList) > 0:
            node = self.header.insert_as_succ(fromList[0])
            self.__size = len(fromList)
            for i in range(1, len(fromList)):
                node = node.insert_as_succ(fromList[i])

    def __str__(self):
        data_list = []
        node = self.header.succ_node

        while node.data is not None:
            data_list.append(node.data)
            node = node.succ_node

        return ', '.join(map(str, data_list))

    def __swap(self, node_p, node_q):
        p_pred = node_p.pred_node
        p_succ = node_p.succ_node

        q_pred = node_q.pred_node
        q_succ = node_q.succ_node

        # node_p and node_q are close to each other
        if node_p.pred_node is node_q:
            q_pred.succ_node = node_p
            node_p.pred_node = q_pred

            node_q.pred_node = node_p
            node_p.succ_node = node_q

            node_q.succ_node = p_succ
            p_succ.pred_node = node_q
        elif node_p.succ_node is node_q:
            self.__swap(node_q, node_p)
        else:
            p_pred.succ_node = node_q
            p_succ.pred_node = node_q

            q_pred.succ_node = node_p
            q_succ.pred_node = node_p

            node_p.pred_node = q_pred
            node_p.succ_node = q_succ

            node_q.pred_node = p_pred
            node_q.succ_node = p_succ

    def reverse(self):
        if (self.__size < 2):
            return

        i = self.__size
        left = self.header.succ_node
        right = self.tailer.pred_node

        while i > 1:
            left = left.succ_node
            right = right.pred_node
            self.__swap(left.pred_node, right.succ_node)
            i -= 2

    def insert_as_first(self, data):
        self.__size += 1
        return self.header.insert_as_succ(data)

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
        node = self.header.succ_node
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
        node = self.header.succ_node
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
        node = self.header.succ_node
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
            self.merge_sort(self.header.succ_node, self.__size)
        else:
            return

    def insert_sort(self):
        if self.__size < 2: return
        node = self.header.succ_node
        r = 0
        while r < self.__size:
            match = self.search(node.data, r, node)
            self.insert_a(self.header if match is None else match, node.data)
            self.remove(node)
            node = node.succ_node
            r += 1

    def selection_sort(self):
        if self.__size < 2:
            return

        def select_max(r):
            max_data = -sys.maxsize - 1
            max_node = None
            node = self.header.succ_node
            n = 0
            while n < r and node.data is not None:
                if node.data > max_data:
                    max_node = node
                    max_data = node.data
                node = node.succ_node
                n += 1
            return max_node

        r = self.__size
        node = self.tailer.pred_node
        while r > 1:
            match = select_max(r)
            self.__swap(node, match)
            node = match.pred_node
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

    def first(self):
        return self.header.succ_node

    def last(self):
        return self.tailer.pred_node

    def empty(self):
        return self.__size == 0

    def set_size(self, size):
        self.__size = size

    def traverse(self, func):
        if self.__size < 1:
            return

        node = self.header.succ_node
        while node.data is not None:
            func(node)
            node = node.succ_node

    def increase(self):
        def addOne(node):
            node.data += 1

        self.traverse(addOne)

    def half(self):
        def halfValue(node):
            node.data /= 2

        self.traverse(halfValue)

    def josephus(self, k):
        if self.__size == 0:
            return None

        n = k
        node = self.header.succ_node

        while self.__size > 1:
            while n > 1:
                n -= 1
                node = node.succ_node
                if node.data is None:
                    node = self.header.succ_node

            self.remove(node)
            node = node.succ_node
            n = k

        return self.header.succ_node
