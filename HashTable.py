import os

from Dictionary import Dictionary
from BitMap import BitMap
from Entry import Entry

class HashTable(Dictionary):

    def __init__(self, c=5):
        self.M = self.__get_prime_number(c)
        self.N = 0
        self.entries = [None] * self.M
        self.lazy_removal = BitMap(self.M)

    def __str__(self):
        values = []
        for entry in self.entries:
            if entry is not None:
                values.append(str(entry.value))

        return ','.join(values)

    def size(self):
        return self.N

    def lazily_removed(self, k):
        return self.lazy_removal.test(k)

    def mark_as_removed(self, k):
        return self.lazy_removal.set(k)

    def put(self, key, value):
        x = self.__probe_for_free(key)
        self.entries[x] = Entry(key, value)
        self.N += 1

        if 2 * self.N > self.M:
            self.__rehash()

    def get(self, key):
        x = self.__probe_for_hit(key)
        entry = self.entries[x]

        return None if entry is None else entry.value

    def remove(self, key):
        x = self.__probe_for_hit(key)
        entry = self.entries[x]

        if entry is not None:
            self.entries[x] = None
            self.mark_as_removed(x)
            self.N -= 1

    def hash_code(self, key):
        if type(key) == int:
            return key
        else:
            return ''.join(str(ord(c)) for c in key)

    def __probe_for_hit(self, key):
        x = key % self.M

        while (self.entries[x] is not None and self.entries[x].key != key) or \
              (self.entries[x] is None and self.lazily_removed(x)):
            x = (x + 1) % self.M

        return x

    def __probe_for_free(self, key):
        x = key % self.M

        while self.entries[x] is not None:
            x = (x + 1) % self.M

        return x

    def __rehash(self):
        old_entries = self.entries

        self.M = self.__get_prime_number(self.M * 2)
        self.entries = [None] * self.M
        self.lazy_removal = BitMap(self.M)
        self.N = 0

        for entry in old_entries:
            if entry is not None:
                self.put(entry.key, entry.value)

    def __get_prime_number(self, m):
        return int(open(os.path.dirname(os.path.abspath(__file__)) + '/prime_number.txt').read().split(',')[m])
