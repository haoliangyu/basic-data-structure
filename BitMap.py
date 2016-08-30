from bitarray import bitarray

class BitMap(object):

    def __init__(self, size=20):
        self.data = size * bitarray([False])

    def set(self, k):
        while k > len(self.data):
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
