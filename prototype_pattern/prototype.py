from abc import abstractmethod, ABCMeta


class Product(metaclass=ABCMeta):
    @abstractmethod
    def use(self, s):
        pass

    @abstractmethod
    def create_clone():
        pass


class Manager:

    def __init__(self):
        self.showcase = {}

    def register(self, name, prototype):
        self.showcase[name] = prototype

    def create(self, protoname):
        p = self.showcase.get(protoname)
        return p.create_clone()


class MessageBox(Product):
    """ メッセージの周りを囲うクラス """
    def __init__(self, deco_char):
        self.deco_char = deco_char

    def use(self, s):
        str_length = len(s) + 4
        print(self.deco_char * str_length)
        print('{0} {1} {0}'.format(self.deco_char, s))
        print(self.deco_char * str_length)
        print('')

    def create_clone(self):
        return self


class UnderlinePen(Product):
    """ メッセージの下線をつけるクラス """
    def __init__(self, ul_char):
        self.ul_char = ul_char

    def use(self, s):
        str_length = len(s)
        print(s)
        print(self.ul_char * str_length)
        print('')

    def create_clone(self):
        return self
