# -------------[Inheritance]----------------
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

class Person:

    def __init__(self, firstname , lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printFullName(self):
        print(f"^^^^^^^^^^ {self.firstname} {self.lastname} ^^^^^^^^^^")


class Student(Person):
    pass

s1 = Student("Elena" , "Shojaei")
s1.printFullName()