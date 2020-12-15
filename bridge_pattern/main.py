from bridge import Display, CountDisplay, RandomCountDisplay, StringDisplayImplement


def main():
    display = Display(StringDisplayImplement('Display Test'))
    count_display = CountDisplay(StringDisplayImplement('CountDisplay Test'))
    random_count_display = RandomCountDisplay(StringDisplayImplement('RandomCountDisplay Test'))

    display.display()
    count_display.multi_display(5)
    random_count_display.random_display(10)


if __name__ == '__main__':
    main()