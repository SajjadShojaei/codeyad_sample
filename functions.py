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