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
        super().__init__(firstname , lastname)             #Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
        self.age = age

    def printAge(self):
        print(f"The age of {self.firstname} is {self.age}")    

s1 = Student("Elena" , "Shojaei" , 6)
s1.printFullName()

# print(s1.age)

s1.printAge()
