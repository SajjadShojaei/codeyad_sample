# -------------[Tuples]----------------
# Tuples are used to store multiple items in a single variable.
# !!! A tuple is a collection which is ordered and unchangeable. !!!
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

models = ('Benz' , 'BMW' , 'Audi' , 'Porshe')
print('models -- lenght=> ' , len(models) , ' \n type=>' , type(models) , '\n data =>' , models , '\n')

# Change Tuple Values

changed_models = list(models)
print('changed_models -- lenght=> ' , len(changed_models) , ' \n type=>' , type(changed_models)  ,'\n data =>' , changed_models , '\n')
changed_models.append('Bently')
new_models = tuple(changed_models)
print('new_models -- lenght=> ' , len(new_models)  ,' \n type=>' , type(new_models)  ,'\n data =>' , new_models , '\n')

# Join Two Tuples
# To join two or more tuples you can use the + operator:

tuple1 = (1,2,3,4,5)
tuple2 = (True,False)
joined_tuples = tuple1 + tuple2
print('joined_tuples -- lenght=> ' , len(joined_tuples)  ,' \n type=>' , type(joined_tuples)  ,'\n data =>' , joined_tuples , '\n')

