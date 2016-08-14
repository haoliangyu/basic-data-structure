import random

from BinNode import BinNode
from BinTree import BinTree

class BinSearchTree(BinTree):

    def search_in(self, node, data, parent):
        if node is None or node.data == data:
            if node.right_child is None or node.right_child.data != data:
                return node

        parent['node'] = node
        next_node = node.left_child if data < node.data else node.right_child
        return self.search_in(next_node, data, parent)

    def search_in_r(self, node, data, parent):
        while node is not None:
            if node.data == data:
                if node.right_child is None or node.right_child.data != data:
                    break

            parent['node'] = node
            node = node.left_child if data < node.data else node.right_child

        return node

    def search(self, data, parent_node):
        return self.search_in_r(self.root, data, parent_node)

    def search_all(self, data):
        parent = { 'node': None }
        node = self.search(data, parent)

        if node is None:
            return []
        else:
            match = []

            while node is not None and node.data == data:
                match.append(node)
                node = node.parent

            return match

    def insert(self, data):
        parent = { 'node': None }
        node = self.search(data, parent)

        if node is None:
            child_node = BinNode(data, parent=parent['node'])
            if data < parent['node'].data:
                parent['node'].left_child = child_node
            else:
                parent['node'].right_child = child_node
        else:
            child_node = BinNode(data, parent=node)
            child_node.right_child = node.right_child
            node.right_child = child_node

        self.update_height_above(child_node)
        self.set_size(self.size() + 1)

        return child_node

    def succ(self, node):
        return None if node.right_child is None else self.__get_succ(node.right_child)

    def __get_succ(self, node):
        return node if node.left_child is None else self.__get_succ(node.left_child)

    def pred(self, node):
        return None if node.left_child is None else self.__get_pred(node.left_child)

    def __get_pred(self, node):
        return node if node.right_child is None else self.__get_pred(node.right_child)

    def remove(self, data):
        parent = { 'node': None }
        node = self.search(data, parent)

        if node is None:
            return False

        self.remove_at(node, parent)
        self.update_height_above(parent['node'])
        self.set_size(self.size() - 1)

        return True

    def remove_at(self, node, parent):
        w = node
        next_node = None

        if not node.has_left_child():
            next_node = node.right_child
        elif not node.has_right_child():
            next_node = node.left_child
        else:
            w = self.succ(w) if random.random() < 0.5 else self.pred(w)
            w.swap(node)

            if w.parent is node:
                if w.data >= node.data:
                    w.parent.right_child = next_node = w.right_child
                else:
                    w.parent.left_child = next_node = w.left_child
            else:
                if w.left_child is None:
                    w.parent.left_child = next_node = w.right_child
                else:
                    w.parent.right_child = next_node = w.left_child

        parent['node'] = w.parent

        if next_node is not None:
            next_node.parent = parent['node']

            if parent['node'] is None:
                self.root = next_node
            elif parent['node'].data < next_node.data:
                parent['node'].right_child = next_node
            else:
                parent['node'].left_child = next_node
        else:
            if w.is_left_child():
                parent['node'].left_child = next_node
            else:
                parent['node'].right_child = next_node

        return next_node

    def zig(self, node):
        left_child = node.left_child

        if node.is_left_child():
            node.parent.left_child = left_child
        else:
            node.parent.right_child = left_child

        left_child.right_child.parent = node
        node.left_child = left_child.right_child

        left_child.right_child = node
        node.parent = left_child

    def zag(self, node):
        right_child = node.right_child

        if node.is_left_child():
            node.parent.left_child = right_child
        else:
            node.parent.right_child = right_child

        right_child.left_child.parent = node
        node.right_child = right_child.left_child

        node.parent = right_child
        right_child.left_child = node

    def stretch_by_zag(self, node):
        height = 1

        end = node
        while end.right_child is not None:
            end = end.right_child

        while node.left_child is not None:
            node = node.left_child

        while node is not end:
            while node.right_child is not None:
                self.zag(node)

            node = node.parent

            height += 1
            node.height += height
