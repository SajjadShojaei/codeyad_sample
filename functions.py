# -------------[Functions]----------------
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

def welcomeMessage():
    print("Hello, My name is Sajji and i hope enjoy my first function in python")

welcomeMessage()


def sum(a , b):
    print(a + b)

sum(2 , 4) # => 6   

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.
def hello(*names):
    for name in names:
        print(f"hello {name}")

hello('ali' , 'sajjad' , 'karim' , 'vahid' , 'majid') # no error if you calling function like this --> hello()

def hello2(fname , lname , *args):
    print(fname)
    print(lname)
    print(args)

hello2('sajjad' , 'shojaei' , 'ali' , 'reza' , 'amir' , 'mahdi') # get error if you calling function like this --> hello2()  ~ 2 arguments is required

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition.

def keyArgs(value1 , value2 , *args , **kwargs):
    print(value1)
    print(value2)
    print(args)
    print(kwargs)

keyArgs('value1' , 'value2' , 'arg1' , 'arg2' , 'arg3' , key1='valueKey1' , key2 ='valueKey2')    


#Another sample

def getUser(first_name , last_name , *args , **kwargs):
    print(first_name)
    print(last_name)
    print(args)
    print(kwargs)

getUser('Sajjad' , 'Shojaei' , 'engineer' , 'artist' , 'player' , age=26 , isAdmin=True) 

# Default Parameter Value
# The following example shows how to use a default parameter value.

def my_function(country = "Iran"):
  print("I am from " + country)

my_function("Sweden") # I am from Sweden
my_function("India")  # I am from India
my_function()         # I am from Iran
my_function("Brazil") # I am from Brazil