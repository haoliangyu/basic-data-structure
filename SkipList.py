import random
from Entry import Entry
from QuadList import QuadList
from Dictionary import Dictionary
from LinkedList import LinkedList

class SkipList(Dictionary, LinkedList):

    def __init__(self):
        super(SkipList, self).__init__()
        self.insert_as_first(QuadList())

        self.__level = 1
        self.__size = 0

    def __str__(self):
        '''print every level of a skip list'''
        levels = []
        qlist = self.first()

        while not qlist.is_tailer():
            count = 1
            level = ''
            node = qlist.data.first()

            while not node.is_tailer():
                level += ' %s~#%d' % (str(node.data.value), count)
                count += 1
                node = node.succ_node

            levels.append(level)
            qlist = qlist.succ_node

        return '\n'.join(levels)

    def size(self):
        return self.__size

    def level(self):
        return self.__level

    def put(self, key, value):
        qlist = self.first()
        p = qlist.data.first()

        # the same process as the skipSearch()
        while True:
            while not p.is_tailer() and p.data.key <= key:
                p = p.succ_node

            p = p.pred_node

            if not p.is_header() and p.data.key == key:
                break

            if p.is_bottom():
                break

            qlist = qlist.succ_node

            p = p.below_node if not p.is_tailer() else qlist.data.first()

        # don't allow duplication
        if not p.is_header() and p.data.key == key:
            return False

        entry = Entry(key, value)
        b = p.insert_as_succ_above(entry)
        qlist = self.last()

        while random.random() < 0.5:
            while not p.is_header() and p.is_roof():
                p = p.pred_node

            if p.is_header():
                if qlist.is_first():
                    new_list = qlist.insert_as_pred(QuadList())

                    qlist.data.header.above_node = new_list.data.header
                    new_list.data.header.below_node = qlist.data.header

                    qlist.data.tailer.above_node = new_list.data.tailer
                    new_list.data.tailer.below_node = qlist.data.tailer

                    self.__level += 1

                p = qlist.pred_node.data.header
            else:
                p = p.above_node

            qlist = qlist.pred_node
            b = p.insert_as_succ_above(entry, b)

        self.__size += 1

        return True

    def get(self, key):
        if self.empty():
            return None

        qlist = self.first()
        result = self.skipSearch(qlist, qlist.data.first(), key)
        return None if result is None else result.data.value


    def remove(self, key):
        qlist = self.first()
        node = self.skipSearch(qlist, qlist.data.first(), key)

        if node is None:
            return False

        while node is not None:
            node.pred_node.succ_node = node.succ_node
            node.succ_node.pred_node = node.pred_node
            node = node.below_node

        row = self.first()
        while self.__level > 1 and row.data.first().is_tailer():
            row.pred_node.succ_node = row.succ_node
            row.succ_node.pred_node = row.pred_node
            row = row.succ_node
            self.__level -= 1

        self.__size -= 1

        return True

    def skipSearch(self, qlist, p, key):
        while True:

            if p.is_header():
                p = p.succ_node

            while not p.is_tailer() and p.data.key <= key:
                p = p.succ_node

            p = p.pred_node

            if not p.is_header() and p.data.key == key:
                return p

            qlist = qlist.succ_node

            p = p.below_node if not p.is_tailer() else qlist.data.first()

    def insert_after_above(self, entry, p, b=None):
        return p.insert_after_above(entry, b)
