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
    print('Yes, "relsID" is one of the keys in the me dictionary')