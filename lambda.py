# -------------[Lambda]----------------
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

x = lambda a , b : a + b 

print(x(14 , 14))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.

def myFunc(n):
    return lambda a : a * n

myDoubler = myFunc(2)

print(myDoubler(3))