users = {
    "sajji" : "1414",
    "amir" : "22222",
    "mohammad" : "5678"
}

entered_username = input('please enter your username: ')
entered_password = input('please enter yout password: ')

# if entered_username not in users and users[entered_username] == entered_password:
#     print('ok, you loged in')
# else:
#     print('ohhhhh nooooo somethings wrong!!')    


while entered_username not in users or users[entered_username] != entered_password:
    entered_username = input('please enter your username agein: ')
    entered_password = input('please enter yout password again: ')

print('ok, you loged in')