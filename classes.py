# -------------[Classes and Objects]----------------
#Python is an object oriented programming language.
#Almost everything in Python is an object, with its properties and methods.

class MyClass:
    x = 5
    Y = 10

p1 = MyClass()
p2 = MyClass()

print(p1.x , p2.Y) # -> 5 10

# The __init__() Function
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

class User:

    def __init__(self , firstName , lastName):
        self.firstName = firstName
        self.lastname = lastName

user1 = User('Sajjad' , 'Shojaei')
user2 = User('Mohammad' , 'Hashemi')

print (user1.firstName) # -> Sajjad
print (user2.lastname) # -> Hashemi


class X:

    def __init__(self):
        print("hello from init()")

a = X() # -> print "hello from init()" , because the init() function called in class X

# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.

class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def about(self):
        print(f"Hey Im {self.name} and my age is {self.age}")    

p1 = Person('Sajjad' , 26)
p1.about() # -> Hey Im Sajjad and my age is 26

# Modify Object Properties
p1.name = 'Ali'
p1.about() # -> Hey Im Ali and my age is 26

# Delete Object Properties
# You can delete properties on objects by using the del keyword: del p1.age