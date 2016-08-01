class BinNode(object):

    def __init__(self, data,
                 parent=None,
                 left_child=None,
                 right_child=None,
                 height=0,
                 npl=1,
                 color='red'):
        self.data = data
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        self.height = height
        self.npl = npl
        self.color = color

    def __str__(self):
        return str(self.data)

    def get_height(self):
        return self.height

    def insert_as_left_child(self, data):
        self.left_child = BinNode(data, self)
        return self.left_child

    def insert_as_right_child(self, data):
        self.right_child = BinNode(data, self)
        return self.right_child

    def swap(self, node):
        cur_parent = self.parent
        cur_left_child = self.left_child
        cur_right_child = self.right_child

        self.parent = node.parent
        self.left_child = node.left_child
        self.right_child = node.right_child

        node.parent = cur_parent
        node.left_child = cur_left_child
        node.right_child = cur_right_child

# **************************************************************************** #
#                             utility function
# **************************************************************************** #

    def is_root(self):
        return self.parent is None

    def is_left_child(self):
        if self.is_root():
            return False

        return self.parent.left_child is self

    def is_right_child(self):
        if self.is_root():
            return False

        return self.parent.right_child is self

    def has_parent(self):
        return not self.is_root()

    def has_left_child(self):
        return self.left_child is not None

    def has_right_child(self):
        return self.right_child is not None

    def has_child(self):
        return self.has_right_child() or self.has_left_child()

    def has_both_child(self):
        return self.has_right_child() and self.has_left_child()

    def is_leaf(self):
        return not self.has_child()

    def sibling(self):
        return self.parent.left_child if self.is_right_child() else self.parent.right_child

    def uncle(self):
        return self.parent.parent.left_child if self.parent.is_right_child() else self.parent.parent.right_child
