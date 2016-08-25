from abc import ABCMeta, abstractmethod

class Dictionary(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def put(self, key, value):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def remove(self, key):
        pass
