class TrieNode(object):

    def __init__(self, char, parent=None, is_str_end=False):
        self.char = char
        self.is_str_end = is_str_end
        self.parent = parent
        self.children = {}

    def is_root(self):
        return self.parent is None

class Trie(object):

    def __init__(self):
        self.__size = 0
        self.root = TrieNode(None)

    def put(self, string):
        node = self.root

        string_length = len(string)
        for i in range(string_length - 1):
            char = string[i]
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char, node)
                node.children[char] = new_node
                node = new_node

        end_char = string[string_length - 1]
        if end_char in node.children:
            node.children[end_char].is_str_end = True
        else:
            node.children[end_char] = TrieNode(end_char, node, True)

        return True

    def exists(self, string):
        return self.search(string) is not None

    def search(self, string):
        node = self.root

        for char in string:
            if char in node.children:
                node = node.children[char]
            else:
                return None

        return node if node.is_str_end else None

    def remove(self, string):
        node = self.search(string)

        if node is None:
            return False

        node.is_str_end = False
        while len(node.children) < 1 and not node.is_root():
            del node.parent.children[node.char]
            node = node.parent

        return True
