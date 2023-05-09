# -------------[For Loops]----------------
# for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters:

for s in "Sajjad":
  print(s)

# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:

friends = ['sajjad' , 'amir' , 'farid' , 'mohammad' , 'ali']
for items in friends:
    if items == 'mohammad':
        break
    print(items)

# The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next: 

books = ["book1", "book2", "book3"]
for book in books:
  if book == "book2":
    continue
  print(book)   