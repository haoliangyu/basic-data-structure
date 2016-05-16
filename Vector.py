import sys

class Vector:
    def __init__(self, fromList=None):
        self.data = [] if fromList is None else fromList

    def __str__(self):
        return str(self.data)

    def __swap(self, n, m):
        temp = self.data[n]
        self.data[n] = self.data[m]
        self.data[m] = temp

    def size(self):
        return len(self.data)

    def find(self, value):
        for i in range(self.size()):
            if self.data[i] == value:
                return i
        return None

    def search(self, value, start=None, end=None):
        start = 0 if start is None else start
        end = self.size() if end is None else end

        while start < end:
            middle = (start + end) // 2
            if value < self.data[middle]:
                end = middle
            else:
                start = middle + 1

        return start - 1

    def bubble_sort(self, lo=None,  hi=None):
        if self.size() < 2:
            return

        lo = 0 if lo is None else lo
        hi = self.size() - 1 if hi is None else hi
        for i in range(lo, hi + 1):
            for j in range(hi):
                if self.data[j] > self.data[j + 1]:
                    self.__swap(j, j + 1)

    def __merge(self, lo, mi, hi):
        array_left = self.data[lo:mi]
        left_length = mi - lo

        array_right = self.data[mi:hi]
        right_length = hi - mi

        i = 0
        j = 0
        k = lo
        while i < left_length or j < right_length:
            if i < left_length and (j == right_length or array_left[i] <= array_right[j]):
                self.data[k] = array_left[i]
                k += 1
                i += 1

            if j < right_length and (i == left_length or array_right[j] < array_left[i]):
                self.data[k] = array_right[j]
                k += 1
                j += 1

    def merge_sort(self, lo=None, hi=None):
        lo = 0 if lo is None else lo
        hi = self.size() if hi is None else hi

        if (hi - lo) < 2:
            return

        middle = (lo + hi) // 2
        self.merge_sort(lo, middle)
        self.merge_sort(middle, hi)

        self.__merge(lo, middle, hi)

    def insert_sort(self, lo=None, hi=None):
        lo = 0 if lo is None else lo
        hi = self.size() if hi is None else hi

        if (hi - lo) < 2:
            return

        i = lo
        while i < hi:
            data = self.data[i]
            match = self.search(data, lo, i) + 1
            del self.data[i]
            self.data.insert(match, data)
            i += 1

    def select_max(self, lo, hi):
        lo = 0 if lo is None else lo
        hi = self.size() if hi is None else hi

        if (hi - lo) < 2:
            return lo

        max_value = -sys.maxsize
        max_index = -1
        for i in range(lo, hi):
            if self.data[i] >= max_value:
                max_value = self.data[i]
                max_index = i

        return max_index

    def selection_sort(self, lo=None, hi=None):
        lo = 0 if lo is None else lo
        hi = self.size() if hi is None else hi

        if (hi - lo) < 2:
            return

        n = hi
        while n > lo:
            match = self.select_max(lo, n)
            self.data.insert(n, self.data[match])
            del self.data[match]
            n -= 1
