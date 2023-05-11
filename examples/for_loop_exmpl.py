names = ['amir' , 'sajjad' , 'ali' , 'majid' , 'farid' , 'mahdi' , 'arshia' , 'sajii']
families = ['sajii' , 'shojaei' , 'khosravi' , 'hashemi' , 'amir']
b = []


for name in names:
    for family in families:
        if name == family:
            b.append(name)

print(b)

name = input("enter you full name: ")
name = name.lower()
name = name.replace(" " , "")

b = []

for n in name:
    if n not in b:
        print(f"your name has {name.count(n)} {n}")
        b.append(n)

# for name in names:
#     if name[-1] == 'i':
#         b.append(name)

# print(b)


#                +++++++++++ THIS IS CODE REFACTORED BT CODEGPT +++++++++++

# names = ['amir', 'sajjad', 'ali', 'majid', 'farid', 'mahdi', 'arshia', 'sajii']
# families = ['sajii', 'shojaei', 'khosravi', 'hashemi', 'amir']

# b = [name for name in names if name in families]
# print(b)

# name = input("Enter your full name: ")
# name = name.lower().replace(" ", "")

# b = []

# for n in set(name):
#     count = name.count(n)
#     print(f"Your name has {count} {n}")
#     b.append(n)
     

