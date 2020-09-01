from singleton import RegisterNote


def main():
    a = RegisterNote.get_instance()
    print(id(a))
    b = RegisterNote.get_instance()
    if id(a) == id(b):
        print('同一のインスタンスIDです')
    a.set_name('a')
    print(a.get_name())
    print(b.get_name())


if __name__ == '__main__':
    main()
