from abc import ABCMeta, abstractmethod


class Aggregate(metaclass=ABCMeta):
    @abstractmethod
    def iterator(self):
        pass


class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def hasNext(self):
        pass

    @abstractmethod
    def next(self):
        pass


class BookShelf(Aggregate):
    def __init__(self, max_size):
        self.books = [] * max_size
        self.shelf_size = max_size

    def get_book_at(self, index):
        return self.books[index]

    def append_book(self, book):
        self.books.append(book)
        self.shelf_size += 1

    def get_length(self):
        return self.shelf_size

    def iterator(self):
        return BookShelfIterator(self)


class Book:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class BookShelfIterator(Iterator):
    def __init__(self, book_shelf):
        self.book_shelf = book_shelf
        self.index = 0

    def hasNext(self):
        return self.index < self.book_shelf.get_length()

    def next(self):
        book = self.book_shelf.get_book_at(self.index)
        self.index += 1
        return book
