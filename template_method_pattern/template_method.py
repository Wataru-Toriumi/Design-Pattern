from abc import abstractmethod, ABCMeta


class AbstractDisplay(metaclass=ABCMeta):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def display(self):
        self.open()
        for i in range(3):
            self.print()
        self.close()


class CharDisplay(AbstractDisplay):
    def __init__(self, ch):
        self.ch = ch

    def open(self):
        print('***')

    def print(self):
        print(self.ch)

    def close(self):
        print('***')