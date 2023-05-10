names = ['amir' , 'sajjad' , 'ali' , 'majid' , 'farid' , 'mahdi' , 'arshia' , 'sajii']

b = []

for name in names:
    if name[-1] == 'i':
        b.append(name)

print(b)