from abc import abstractmethod, ABCMeta


class Product(metaclass=ABCMeta):
    """プロトタイプで実装する必要のあるメソッドを定義した抽象クラス"""

    @abstractmethod
    def use(self, string: str) -> None:
        """定型処理を行うメソッド"""
        pass

    @abstractmethod
    def create_clone(self) -> Product:
        """クローンを生成するメソッド"""
        pass


class MessageBox(Product):
    """メッセージの周りを囲うクラス"""

    def __init__(self, deco_char):
        self.deco_char = deco_char

    def use(self, string: str) -> None:
        str_length = len(string) + 4
        print(self.deco_char * str_length)
        print('{0} {1} {0}'.format(self.deco_char, string))
        print(self.deco_char * str_length)
        print('')

    def create_clone(self) -> Product:
        return self


class UnderlinePen(Product):
    """メッセージの下線をつけるクラス"""

    def __init__(self, ul_char):
        self.ul_char = ul_char

    def use(self, string: str) -> None:
        str_length = len(string)
        print(string)
        print(self.ul_char * str_length)
        print('')

    def create_clone(self) -> Product:
        return self


class Manager:
    """プロトタイプの管理を行うクラス"""

    def __init__(self):
        self.showcase = {}

    def register(self, name: str, prototype: Product) -> None:
        self.showcase[name] = prototype

    def create(self, name: str):
        p = self.showcase.get(name)
        return p.create_clone()
