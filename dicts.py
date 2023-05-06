# -------------[Dictionaries]----------------
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
me = {
    "name" : "Sajji",
    "lastName" : "Shojaei",
    "age" : 26,
    "isAdmin" : True,
    "relsID" : ['2324' , '1213' , '46']
}
print('dictionary -- lenght=> ' , len(me)  ,' \n type=>' , type(me)  ,'\n data =>' , me , '\n')

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:

myAge = me['age']
print('myAge -- lenght=> ' ,' \n type=>' , type(myAge)  ,'\n data =>' , myAge , '\n')

# There is also a method called get() that will give you the same result:

myName = me.get('name')
print('myName -- lenght=> ' , len(myName)  ,' \n type=>' , type(myName)  ,'\n data =>' , myName , '\n')

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.

getKeys = me.keys()
print('getKeys -- lenght=> ' , len(getKeys)  ,' \n type=>' , type(getKeys)  ,'\n data =>' , getKeys , '\n')

# Get Values
# The values() method will return a list of all the values in the dictionary.

getValues = me.values()
print('getValues -- lenght=> ' , len(getValues)  ,' \n type=>' , type(getValues)  ,'\n data =>' , getValues , '\n')

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.

getItems = me.items()
print('getItems -- lenght=> ' , len(getItems)  ,' \n type=>' , type(getItems)  ,'\n data =>' , getItems , '\n')

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:

if 'relsID' in me:
    print('Yes, "relsID" is one of the keys in the me dictionary \n')

# Change Values
# You can change the value of a specific item by referring to its key name:

me['isAdmin'] = False
print('changed_dict -- lenght=> ' , len(me)  ,' \n type=>' , type(me)  ,'\n data =>' , me , '\n')

# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.  

me.update({'phoneNumber': '09332827748'})
print('updated_dict -- lenght=> ' , len(me)  ,' \n type=>' , type(me)  ,'\n data =>' , me , '\n')

# Removing Items
# The pop() method removes the item with the specified key name:

me.pop('isAdmin')
print('removed_item_pop_dict -- lenght=> ' , len(me)  ,' \n type=>' , type(me)  ,'\n data =>' , me , '\n')

# The popitem() method removes the last inserted item:

me.popitem()
print('removed_item_popitem_dict -- lenght=> ' , len(me)  ,' \n type=>' , type(me)  ,'\n data =>' , me , '\n')

# The del keyword removes the item with the specified key name:

# del me['isAdmin']
print('removed_item_ del_dict -- lenght=> ' , len(me)  ,' \n type=>' , type(me)  ,'\n data =>' , me , '\n')

# The clear() method empties the dictionary:

# me.clear()
print('removed_item_clear_dict -- lenght=> ' , len(me)  ,' \n type=>' , type(me)  ,'\n data =>' , me , '\n')


# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

copiedDict = me.copy()
copiedDict['colorEyes'] = 'brown'
print('copied_dict -- lenght=> ' , len(copiedDict)  ,' \n type=>' , type(copiedDict)  ,'\n data =>' , copiedDict , '\n')

# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print('nested_dict -- lenght=> ' , len(copiedDict)  ,' \n type=>' , type(copiedDict)  ,'\n data =>' , myfamily["child2"]["name"] , '\n')
