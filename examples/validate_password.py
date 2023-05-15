# example the validation enter passwords:

def validationPass(password):
    if len(password) < 8:
        print(f"Your {password} must be at least 8 char")
    elif password.isnumeric():
        print(f"Your {password} must be at least one letter")
    elif password.isalpha():
        print(f"Your {password} must be at least one number")
    else:
        print("Your password is validate!")            

while True:
    password = input("enter your password: ")
    validationPass(password)