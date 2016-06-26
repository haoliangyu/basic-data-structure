from bitarray import bitarray

class BitMap(object):

    def __init__(self):
        self.data = 20 * bitarray([False])

    def set(self, k):
        if k > len(self.data):
            self.data = (len(self.data) * bitarray([False])).extend(self.data)

        self.data[k] = True

    def clear(self, k):
        if k > len(self.data):
            self.data = (len(self.data) * bitarray('0')).extend(self.data)

        self.data[k] = False

    def test(self, k):
        if k > len(self.data):
            self.data = (len(self.data) * bitarray('0')).extend(self.data)

        return self.data[k]
