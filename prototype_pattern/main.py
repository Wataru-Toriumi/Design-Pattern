from prototype import Manager, MessageBox, UnderlinePen


def main():
    manager = Manager()
    upen = UnderlinePen('-')
    mbox = MessageBox('@')
    sbox = MessageBox('$')

    manager.register('strong message', upen)
    manager.register('warning box', mbox)
    manager.register('slash box', sbox)

    p1 = manager.create('strong message')
    p1.use('Git Hub')
    p2 = manager.create('warning box')
    p2.use('Qiita')
    p3 = manager.create('slash box')
    p3.use('Java')


if __name__ == '__main__':
    main()
