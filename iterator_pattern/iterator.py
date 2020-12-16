from abc import ABCMeta, abstractmethod


class Aggregate(metaclass=ABCMeta):
    """シーケンスを定義する抽象クラス"""

    @abstractmethod
    def iterator(self):
        """イテレーションするように抽象メソッドを用意"""
        pass


class Iterator(metaclass=ABCMeta):
    """イテレーションを定義する抽象クラス"""

    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


class BookShelf(Aggregate):
    """本のイテレーションを定義しているクラス"""

    def __init__(self):
        self.books = []
        self.shelf_size = 0

    def get_book_at(self, index) -> Book:
        return self.books[index]

    def append_book(self, book: Book) -> None:
        self.books.append(book)
        self.shelf_size += 1

    def get_length(self) -> int:
        return self.shelf_size

    def iterator(self) -> BookShelfIterator:
        return BookShelfIterator(self)


class Book:
    """本の定義をまとめたクラス"""

    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name


class BookShelfIterator(Iterator):
    """本のイテレーションを定義したクラス"""

    def __init__(self, book_shelf: BookShelf) -> None:
        self.book_shelf = book_shelf
        self.index = 0

    def has_next(self) -> bool:
        return self.index < self.book_shelf.get_length()

    def next(self) -> Book:
        book = self.book_shelf.get_book_at(self.index)
        self.index += 1
        return book
