x=input("enter string:")
x=x.split()
z=[]
for i in x:
    if i in z:
        pass
    else:
        z.append(i)
z=tuple(z)
print(z)