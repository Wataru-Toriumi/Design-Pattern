from abc import abstractmethod, ABCMeta


class Product(metaclass=ABCMeta):
    @abstractmethod
    def use(self):
        pass


class Factory(metaclass=ABCMeta):
    def create(self, owner):
        product = self.create_product(owner)
        self.register_product(product)
        return product

    @abstractmethod
    def create_product(self, owner):
        pass

    @abstractmethod
    def register_product(self, product):
        pass


class AccountFactory(Factory):
    def __init__(self):
        self.owners = []

    def create_product(self, owner):
        return Account(owner)

    def register_product(self, product):
        self.owners.append(product.get_owner())


class Account(Product):
    def __init__(self, owner):
        print('Create account: {}'.format(owner))
        self.owner = owner

    def use(self):
        print('Use account: {}'.format(self.owner))

    def get_owner(self):
        return self.owner
