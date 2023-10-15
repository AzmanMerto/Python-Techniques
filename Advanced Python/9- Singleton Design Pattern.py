from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def print_data():
        """ Implement Data """

class PersonSingelton(IPerson):

    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingelton.__instance == None:
            PersonSingelton("Default Name", 0)
        return PersonSingelton.__instance

    def __init__(self, name, age):
        if PersonSingelton.__instance != None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.name = name
            self.age = age
            PersonSingelton.__instance = self

    @staticmethod
    def print_data():
        print(f"Name: {PersonSingelton.__instance.name} Age: {PersonSingelton.__instance.age}")

p = PersonSingelton("Mert", 31)

print(p)
p.print_data()