# -------------[strings]----------------

firstName = 'sajjai'
lastName = 'shojaei'
city = 'mashhad'


me = f'my name is: {firstName} {lastName} and Im from {city}!'
# print(me.count(''))

# -------------[operators]----------------

pass1 = '12345'
pass2 = '1235'

# print(pass1 == pass2)
# print(pass1 != pass2)
# print(pass1 > pass2)

# # -------------[value from input]----------------

# first_number = input("choose a number between 1 - 9 : ")
# first_number = int(first_number)
# first_number *= 2

# print(first_number)

# -------------[lists]----------------

mylist = ['sajjad' , 'ali' , 'mamad']
mylist[1] = 'reza'
mylist.insert(2 , 'yousef')
mylist.append('amir')
# print('lenght=> ' , len(mylist) ,'|| data =>' , mylist)

friends = ['sajjad' , 'ali' , 'mamad','sajjad' , 'ali' , 'mamad']
friends.remove('ali')
friends.pop(4)
del friends[1]
friends.clear()
# print('friends -- lenght=> ' , len(friends) ,'|| data =>' , friends)

alphabet_list = ['c' , 'j' , 'a' , 'e' , 'h' , 'g' , 'b' , 'i' , 'd' , 'f']
# print('alphabet_list -- lenght=> ' , len(alphabet_list) ,'|| data =>' , alphabet_list)
alphabet_list.sort()
# print('alphabet_list --lenght=> ' , len(alphabet_list) ,'|| data =>' , alphabet_list)

numbers_list = [43, 2 , 12 , 14 , 15 , 65, 9 , 24]
# print('numbers_list -- lenght=> ' , len(numbers_list) ,'|| data =>' , numbers_list)
numbers_list.sort(reverse=True)
# print('numbers_list -- lenght=> ' , len(numbers_list) ,'|| data =>' , numbers_list)
copy_number_list = numbers_list.copy()
# print('copy_number_list -- lenght=> ' , len(copy_number_list) ,'|| data =>' , copy_number_list)

joined_list = alphabet_list + numbers_list
print('joined_list -- lenght=> ' , len(joined_list) ,'|| data =>' , joined_list)



# ---------------------------------
