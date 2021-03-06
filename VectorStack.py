import random

from Vector import Vector

class VectorStack(Vector):

    def __init__(self, fromList=None):
        Vector.__init__(self, fromList)

    def empty(self):
        return self.size() == 0

    def push(self, data):
        self.data.append(data)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1] if self.size() > 0 else None

    def permutate(self):
        s = VectorStack()
        b = VectorStack()

        while self.size() > 0:
            if s.size() == 0:
                s.push(self.pop())
            else:
                coin = random.random()
                if coin < 0.5:
                    s.push(self.pop())
                else:
                    b.push(s.pop())

        while s.size() > 0:
            b.push(s.pop())

        return b

    def get_data(self):
        stack_data = [self.data[i] for i in range(self.size())]
        return stack_data

    def equals(self, stack):
        if self.size() != stack.size():
            return False

        stack_data = stack.get_data()

        n = self.size()
        i = 0
        while i < n:
            if self.data[i] != stack_data[i]:
                return False
            i += 1

        return True

    def clear(self):
        while not self.empty():
            self.pop()
