from BinSearchTree import BinSearchTree
from BinNode import BinNode

class AVLTree(BinSearchTree):

    def insert(self, data):
        parent = { 'node': None }
        x = self.search(data, parent)
        if x is not None:
            return x

        x = BinNode(data, parent['node'])
        if x.data < parent['node'].data:
            parent['node'].left_child = x
        else:
            parent['node'].right_child = x

        self.set_size(self.size() + 1)

        node = parent['node']
        while node is not None:
            if not self.is_avl_balanced(node):
                is_left_child = None
                if not node.is_root():
                    is_left_child = node.is_left_child()

                rebalanced = self.__rotate_at(self.taller_child(self.taller_child(node)))

                if is_left_child is None:
                    self.root = rebalanced
                elif is_left_child:
                    rebalanced.parent.left_child = rebalanced
                else:
                    rebalanced.parent.right_child = rebalanced
                break
            else:
                self.update_height(node)

            node = node.parent

        return x

    def remove(self, data):
        parent = { 'node': None }
        x = self.search(data, parent)
        if x is None:
            return False

        self.remove_at(x, parent)
        self.set_size(self.size() - 1)

        node = parent['node']
        while node is not None:
            if not self.is_avl_balanced(node):
                is_left_child = None
                if not node.is_root():
                    is_left_child = node.is_left_child()

                rebalanced = self.__rotate_at(self.taller_child(self.taller_child(node)))

                if is_left_child is None:
                    self.root = rebalanced
                elif is_left_child:
                    rebalanced.parent.left_child = rebalanced
                else:
                    rebalanced.parent.right_child = rebalanced

            self.update_height(node)
            node = node.parent

        return True


    def is_balanced(self, node):
        return self.stature(node.left_child) == self.stature(node.right_child)

    def balance_factor(self, node):
        return self.stature(node.left_child) - self.stature(node.right_child)

    def is_avl_balanced(self, node):
        return -2 < self.balance_factor(node) < 2

    def stature(self, node):
        if node is None:
            return 0

        left_stature = self.stature(node.left_child)
        right_stature = self.stature(node.right_child)

        return (left_stature if left_stature > right_stature else right_stature) + 1

    def taller_child(self, node):
        stature_left = self.stature(node.left_child)
        stature_right = self.stature(node.right_child)

        if stature_left < stature_right:
            return node.right_child
        elif stature_left > stature_right:
            return node.left_child
        else:
            return node.left_child if node.is_left_child() else node.right_child

    def __connect34(self, a, b, c, t0, t1, t2, t3):
        a.left_child = t0
        if t0 is not None:
            t0.parent = a

        a.right_child = t1
        if t1 is not None:
            t1.parent = a

        self.update_height(a)

        c.left_child = t2
        if t2 is not None:
            t2.parent = c

        c.right_child = t3
        if t3 is not None:
            t3.parent = c

        self.update_height(c)

        b.left_child = a
        b.right_child = c

        a.parent = b
        c.parent = b

        self.update_height(b)

        return b

    def __rotate_at(self, v):
        p = v.parent
        g = p.parent

        if p.is_right_child():
            if v.is_right_child():
                p.parent = g.parent
                return self.__connect34(g, p, v, g.left_child, p.left_child, v.left_child, v.right_child)
            else:
                v.parent = g.parent
                return self.__connect34(g, v, p, g.left_child, v.left_child, v.right_child, p.right_child)
        else:
            if v.is_left_child():
                p.parent = g.parent
                return self.__connect34(v, p, g, v.left_child, v.right_child, p.right_child, g.right_child)
            else:
                v.parent = g.parent
                return self.__connect34(p, v, g, p.left_child, v.left_child, v.right_child, g.right_child)
