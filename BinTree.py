from BinNode import BinNode

class BinTree(object):

    def __init__(self):
        self.root = None
        self.__size = 0

    def size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

    def update_height(self, node):
        left_height = -1 if node.left_child is None else node.left_child.get_height()
        right_height = -1 if node.right_child is None else node.right_child.get_height()
        node.height = 1 + left_height if left_height > right_height else right_height
        return node.height

    def calculate_height(self, node):
        left_height = -1 if node.left_child is None else node.left_child.get_height()
        right_height = -1 if node.right_child is None else node.right_child.get_height()

        return 1 + left_height if left_height > right_height else right_height

    def update_height_above(self, node):
        while node is not None:
            height = self.calculate_height(node)

            if node.height == height:
                return

            node.height = height
            node = node.parent

    def insert_as_root(self, data):
        self.root = BinNode(data)
        self.__size = 1
        return self.root

    def insert_as_left_child(self, parent, data):
        parent.insert_as_left_child(data)
        self.update_height_above(parent)
        self.__size += 1
        return parent.left_child

    def insert_as_right_child(self, parent, data):
        parent.insert_as_right_child(data)
        self.update_height_above(parent)
        self.__size += 1
        return parent.right_child

    def attach_as_left_child(self, parent, tree):
        parent.left_child = tree.root
        self.__size += tree.size()
        self.update_height_above(parent)
        return parent

    def attach_as_right_child(self, parent, tree):
        parent.right_child = tree.root
        self.__size += tree.size()
        self.update_height_above(parent)
        return parent

    def remove(self, node):
        if node.is_root():
            return self.__size
        elif node.is_left_child():
            node.parent.left_child = None
        else:
            node.parent.right_child = None

        remove_count = self.remove_at(node)
        self.update_height_above(node.parent)
        self.__size -= remove_count
        return remove_count

    def remove_at(self, node):
        if node is None: return 0
        return 1 + self.remove_at(node.left_child) + self.remove_at(node.right_child)

    def secede(self, node):
        if node.is_root():
            return node
        elif node.is_left_child():
            node.parent.left_child = None
        else:
            node.parent.right_child = None

        remove_count = self.remove_at(node)
        self.update_height_above(node.parent)
        self.__size -= remove_count

        new_tree = BinTree()
        new_tree.root = node
        new_tree.__size = remove_count
        node.parent = None

        return new_tree

    def trav_pre_r(self, node, visit):
        if node is None:
            return

        visit(node)
        self.trav_pre_r(node.left_child, visit)
        self.trav_pre_r(node.right_child, visit)

    def trav_post_r(self, node, visit):
        if node is None:
            return

        self.trav_pre_r(node.left_child, visit)
        self.trav_pre_r(node.right_child, visit)
        visit(node)

    def trav_in_r(self, node, visit):
        if node is None:
            return

        self.trav_pre_r(node.left_child, visit)
        visit(node)
        self.trav_pre_r(node.right_child, visit)
