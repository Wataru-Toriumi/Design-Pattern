from abc import ABCMeta, abstractmethod
import random

class Display:
    """表示を扱うクラス"""

    def __init__(self, impl) -> None:
        self.__impl = impl

    def open(self) -> None:
        self.__impl.raw_open()

    def print(self) -> None:
        self.__impl.raw_print()

    def close(self) -> None:
        self.__impl.raw_close()

    def display(self) -> None:
        self.open()
        self.print()
        self.close()


class CountDisplay(Display):
    """表示回数を指定したクラス"""

    def multi_display(self, times: int) -> None:
        self.open()
        for _ in range(times):
            self.print()
        self.close()


class RandomCountDisplay(CountDisplay):
    """表示回数がランダムに指定されるクラス"""

    def random_display(self, times: int) -> None:
        self.multi_display(random.randint(0, times))


class DisplayImplement(metaclass=ABCMeta):
    """実装クラス"""

    @abstractmethod
    def raw_open(self) -> None:
        pass

    @abstractmethod
    def raw_print(self) -> None:
        pass

    @abstractmethod
    def raw_close(self) -> None:
        pass


class StringDisplayImplement(DisplayImplement):
    """文字列を使用した表示を行うクラス"""

    def __init__(self, string: str) -> None:
        self.string = string
        self.width = len(string)

    def raw_open(self) -> None:
        self.print_line()

    def raw_print(self) -> None:
        print(f'|{self.string}|')

    def raw_close(self) -> None:
        self.print_line()

    def print_line(self) -> None:
        print('+', end='')
        for i in range(self.width):
            print('-', end='')
        print('+')
