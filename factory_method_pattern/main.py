from factory_method import AccountFactory


def main():
    factory = AccountFactory()
    account1 = factory.create('Github')
    account2 = factory.create('Bitbucket')

    account1.use()
    account2.use()


if __name__ == '__main__':
    main()
