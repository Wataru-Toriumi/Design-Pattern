from abc import ABCMeta, abstractmethod


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(self.name)

    def print_age(self):
        print(self.age)


class Student(metaclass=ABCMeta):
    @abstractmethod
    def show_name(self):
        pass

    @abstractmethod
    def show_age(self):
        pass


class HumanAdapter(Student):
    def __init__(self, name, age):
        self.human = Human(name, age)

    def show_name(self):
        self.human.print_name()

    def show_age(self):
        self.human.print_age()
