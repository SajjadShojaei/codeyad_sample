names = ['amir' , 'sajjad' , 'ali' , 'majid' , 'farid' , 'mahdi' , 'arshia' , 'sajii']
families = ['sajii' , 'shojaei' , 'khosravi' , 'hashemi' , 'amir']
b = []


for name in names:
    for family in families:
        if name == family:
            b.append(name)

print(b)

# for name in names:
#     if name[-1] == 'i':
#         b.append(name)

# print(b)