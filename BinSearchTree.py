from BinNode import BinNode
from BinTree import BinTree

class BinSearchTree(BinTree):

    def search_in(self, node, data, parent):
        if node is None or node.data == data:
            return node
        parent['node'] = node
        next_node = node.left_child if data < node.data else node.right_child
        return self.search_in(next_node, data, parent)

    def search(self, data, parent_node):
        return self.search_in(self.root, data, parent_node)

    def insert(self, data):
        parent = { 'node': None }
        node = self.search(data, parent)

        if node is not None:
            return None

        child_node = BinNode(data, parent=parent['node'])

        if data < parent['node'].data:
            parent['node'].left_child = child_node
        else:
            parent['node'].right_child = child_node

        self.update_height_above(child_node)
        self.__size += 1

        return child_node

    def succ(self, node):
        return None if node.right_child is None else self.__get_succ(node.right_child)

    def __get_succ(self, node):
        return node if node.left_child is None else self.__get_succ(node.left_child)

    def remove(self, data):
        parent = { 'node': None }
        node = self.search(data, parent)

        if node is None:
            return False

        self.remove_at(node, parent)
        self.update_height_above(parent['node'])
        self.__size -= 1

        return True

    def remove_at(self, node, parent):
        w = node
        succ = None

        if not node.has_left_child():
            succ = node = node.right_child
        elif not node.has_right_child():
            succ = node = node.left_child
        else:
            w = self.succ(w)
            w.swap(node)

            w_parent = w.parent
            if w_parent is node:
                w_parent.right_child = succ = w.right_child
            else:
                w_parent.left_child = succ = w.right_child

        parent['node'] = w.parent

        if succ is not None:
            succ.parent = parent['node']

        return succ
