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
