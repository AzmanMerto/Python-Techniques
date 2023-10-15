class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return  self.__name

    @property
    def Age(self):
        return self.__age
    @Name.setter
    def name(self, value):
        self.__name = value

    @Age.setter
    def age(self, value):
        self.__age = value

    @staticmethod
    def myMethod():
        print("Hello world")

p1 = Person("Mert", 23, "male")

p1.myMethod()

print(p1.Age)
p1.age = 31
print(p1.Age)