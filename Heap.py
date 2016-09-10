class Heap(object):

    def __init__(self, data=[]):
        self.data = data
        self.__size = len(data)
        self.__heapify()

    def size(self):
        return self.__size

    def empty(self):
        return self.__size == 0

    def get_max(self):
        return self.data[0]

    def delete_max(self):
        max_data = self.data[0]
        self.__swap(0, self.size() - 1)
        self.__size -= 1

        self.__percolate_down(0)

        return max_data

    def insert(self, number):
        self.__size += 1
        self.data[self.__size - 1] = number

        return self.__percolate_up(self.size() - 1)

    @staticmethod
    def heap_sort(data):
        heap = Heap(data)
        index = heap.size() - 1

        while not heap.empty():
            heap.data[index] = heap.delete_max()
            index -= 1

        return heap.data

    def __percolate_down(self, i):
        current_index = i
        potential_parent = self.__proper_parent(current_index)

        while self.data[potential_parent] > self.data[current_index]:
            self.__swap(potential_parent, current_index)
            current_index = potential_parent
            potential_parent = self.__proper_parent(current_index)

        return current_index

    def __percolate_up(self, i):
        current_index = i

        while self.__has_parent(current_index):
            parent_index = self.__parent(current_index)

            if self.data[current_index] <= self.data[parent_index]:
                return current_index
            else:
                self.__swap(current_index, parent_index)
                current_index = parent_index

        return 0

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
