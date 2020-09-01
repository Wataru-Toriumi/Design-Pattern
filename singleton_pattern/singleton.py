class RegisterNote(object):
    __instance = None

    def __init__(self):
        if self.__instance:
            raise Exception('Not allowed')

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = cls()
        return cls.__instance

    @classmethod
    def set_name(cls, name):
        cls.name = name

    @classmethod
    def get_name(cls, name):
        return cls.name
