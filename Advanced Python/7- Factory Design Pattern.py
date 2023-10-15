from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass = ABCMeta):

    @abstractstaticmethod
    def person_method():
        """ Interface Method """

class Student(IPerson):

    def __init__(self):
        self.name = "Basic Student Name"

    def person_method(self):
        print("I am student")

class Teacher(IPerson):

    def __init__(self):
        self.name = "Basic Teacher Name"

    def person_method(self):
        print("I am Teacher")

class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        elif person_type == "Teacher":
            return Teacher()

if __name__ == "__main__":
    choice = input("Type: ")
    person = PersonFactory.build_person(choice)
    person.person_method()