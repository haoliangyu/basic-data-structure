class QuadListNode(object):

    def __init__(self, entry=None, pred=None, succ=None, above=None, below=None):
        self.data = entry
        self.pred_node = pred
        self.succ_node = succ
        self.above_node = above
        self.below_node = below

    def insert_as_succ_above(self, data, below=None):
        node = QuadListNode(data, self, self.succ_node, None, below)

        self.succ_node.pred_node = node
        self.succ_node = node

        if below is not None:
            below.above_node = node

        return node

    def is_header(self):
        return self.pred_node is None

    def is_tailer(self):
        return self.succ_node is None

    def is_roof(self):
        return self.above_node is None

    def is_bottom(self):
        return self.below_node is None
