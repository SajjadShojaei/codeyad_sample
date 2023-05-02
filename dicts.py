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

