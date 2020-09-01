from singleton import RegisterNote


def main():
    a = RegisterNote.get_instance()
    print(id(a))
    b = RegisterNote.get_instance()
    print(id(a) == id(b))


if __name__ == '__main__':
    main()
