class Heap(object):

    def __init__(self, data=[]):
        if len(data) == 0:
            self.data = [None] * 100
        else:
            self.data = data

        self.__size = sum([1 if item is not None else 0 for item in self.data])
        self.__heapify()

    def size(self):
        return self.__size

    def empty(self):
        return self.__size == 0

    def get_max(self):
        return self.data[0]

    def delete_max(self):
        max_data = self.data[0]
        self.__swap(0, self.__size - 1)
        self.data[self.__size - 1] = None
        self.__size -= 1

        self.__percolate_down(0)

        return max_data

    def insert(self, number):
        if self.__size == len(self.data):
            self.__expand()

        self.__size += 1
        self.data[self.__size - 1] = number

        return self.__percolate_up(self.__size - 1)

    @staticmethod
    def heap_sort(data):
        heap = Heap(data)
        index = heap.size() - 1

        while not heap.empty():
            heap.data[index] = heap.delete_max()
            index -= 1

        return heap.data

    def __percolate_down(self, i):
        initial_value = self.data[i]
        current_index = i
        potential_parent = self.__proper_parent(current_index)

        while self.data[potential_parent] > self.data[current_index]:
            self.data[current_index] = self.data[potential_parent]
            current_index = potential_parent
            potential_parent = self.__proper_parent(current_index)

        self.data[current_index] = initial_value

        return current_index

    def __percolate_up(self, i):
        if not self.__has_parent(i):
            return 0

        initial_value = self.data[i]
        parent_indexes = []

        h = 1
        current_index = i
        while self.__has_parent(current_index):
            current_index = ((i + 1) >> h) - 1
            parent_indexes.append(current_index)
            h += 1

        lo = 0
        hi = len(parent_indexes) - 1
        while lo + 1 < hi:
            mi = (lo + hi) / 2

            if self.data[parent_indexes[mi]] <= self.data[i]:
                lo = mi
            else:
                hi = mi


        parent_indexes.insert(0, i)
        lo = lo + 1
        index = 0
        while index < lo:
            self.data[parent_indexes[index]] = self.data[parent_indexes[index + 1]]
            index += 1

        self.data[parent_indexes[lo]] = initial_value

        return parent_indexes[lo]

    def __expand(self):
        new_data = [None] * (self.__size * 2)
        for i in range(self.__size):
            new_data[i] = self.data[i]

        self.data = new_data

    def __heapify(self):
        i = self.__last_internal()

        while self.__in_heap(i):
            self.__percolate_down(i)
            i -= 1

    def __swap(self, i , j):
        temp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = temp

    def __in_heap(self, i):
        return 0 <= i < self.size()

    def __parent(self, i):
        return (i - 1) >> 1

    def __last_internal(self):
        return self.__parent(self.size() - 1)

    def __left_child(self, i):
        return (i << 1) + 1

    def __right_child(self, i):
        return (i + 1) << 1

    def __has_parent(self, i):
        return 0 < i

    def __has_left_child(self, i):
        return self.__in_heap(self.__left_child(i))

    def __has_right_child(self, i):
        return self.__in_heap(self.__right_child(i))

    def __bigger(self, i, j):
        return i if self.data[i] > self.data[j] else j

    def __proper_parent(self, i):
        return self.__bigger(self.__bigger(self.__left_child(i), self.__right_child(i)), i) if self.__has_right_child(i) else \
               self.__bigger(self.__left_child(i), i) if self.__has_left_child(i) else \
               i
