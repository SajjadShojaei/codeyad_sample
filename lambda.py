# -------------[Lambda]----------------
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

x = lambda a , b : a + b 

print(x(14 , 14)) # -> 28

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.

def myFunc(n):
    return lambda a : a * n

myDoubler = myFunc(2)

print(myDoubler(3)) # -> 6


# Use lambda in map() function
mylist = [1,2,3,5,6,7,8,9]
z = map(lambda a : a * 2 , mylist)
print(list(z)) # -> [2, 4, 6, 10, 12, 14, 16, 18]
