from iterator import BookShelf, Book


def main():
    book_shelf = BookShelf()

    book_shelf.append_book(Book('github'))
    book_shelf.append_book(Book('qiita'))
    book_shelf.append_book(Book('java'))
    book_shelf.append_book(Book('iterator pattern'))

    iterator = book_shelf.iterator()
    while(iterator.has_next()):
        book = iterator.next()
        print(book.get_name())


if __name__ == '__main__':
    main()
