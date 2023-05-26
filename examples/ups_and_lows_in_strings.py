
def checkUpsAndLows(name):
    ups = 0
    lows = 0
    for n in name:
        if n.isupper():
            ups += 1
        elif n.islower():
            lows += 1
        else :
            pass

    print(f"upper cases: {ups}")                
    print(f"upper cases: {lows}")

# don't stop app
while True:
    name = input("enter your name:")
    checkUpsAndLows(name)                    