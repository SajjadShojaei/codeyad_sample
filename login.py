stored_pass = "12345"

entered_pass = input('enter your password: ')

#              This is bad method ;(

# if entered_pass == stored_pass:
#     print("greate, you are logged successfully")
# else:
#     print("ooooh you are wrong!!")   

#              This is good method ;)

while entered_pass != stored_pass:
    entered_pass = input('oooh you are wrong, please enter again: ')

print("greate, you are logged successfully")   
