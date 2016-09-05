import os

from LinkedList import Node

class Bucket(object):

    def sort(self, values):
        n = len(values) * 2
        m = self.__get_prime_number(n)
        bucket = [None] * n

        # insert into value list
        for value in values:
            key = value % m

            new_node = Node(value)
            if bucket[key] is None:
                bucket[key] = new_node
            else:
                node = bucket[key]
                while node.succ_node is not None:
                    node = node.succ_node

                node.succ_node = new_node
                new_node.pred_node = node

        # get sorted values
        sorted_values = []
        for item in bucket:
            if item is None:
                continue

            node = item
            while node is not None:
                sorted_values.append(node.data)
                node = node.succ_node

        return sorted_values

    def __get_prime_number(self, n):
        return int(open(os.path.dirname(os.path.abspath(__file__)) + '/prime_number.txt').read().split(',')[n])
