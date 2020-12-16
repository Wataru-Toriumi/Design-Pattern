from prototype import Manager, MessageBox, UnderlinePen


def main():
    manager = Manager()
    # プロトタイプの生成
    upen = UnderlinePen('-')
    mbox = MessageBox('@')
    sbox = MessageBox('$')

    # プロトタイプを登録
    manager.register('strong message', upen)
    manager.register('warning box', mbox)
    manager.register('slash box', sbox)

    # プロトタイプのクローンの生成と使用
    p1 = manager.create('strong message')
    p1.use('Git Hub')
    p2 = manager.create('warning box')
    p2.use('Qiita')
    p3 = manager.create('slash box')
    p3.use('Java')


if __name__ == '__main__':
    main()
