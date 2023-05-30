# -------------[Inheritance]----------------
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

class Person:  #Parent

    def __init__(self, firstname , lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printFullName(self):
        print(f"^^^^^^^^^^ {self.firstname} {self.lastname} ^^^^^^^^^^")


class Student(Person):   #Child
    
    def __init__(self, firstname, lastname , age):
        # Person.__init__(self ,firstname, lastname)
        super().__init__(firstname , lastname)
        self.age = age

s1 = Student("Elena" , "Shojaei" , 6)
s1.printFullName()

print(s1.age)