from adapter import HumanAdapter


def main():
    student = HumanAdapter('田中', 25)
    student.show_name()
    student.show_age()


if __name__ == '__main__':
    main()